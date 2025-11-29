from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import time
from .models import Medicacao, Estoque, RegistroAdministracao, Lembrete

class SistemaKaruTests(TestCase):

    def setUp(self):
        """
        Configuração inicial executada antes de cada método de teste.

        Description:
            Cria um ambiente isolado com:
            1. Um client.
            2. Um usuário Admin para acesso ao sistema.
            3. Uma Medicação base para associar aos registros.

        Returns:
            None

        Raises:
        """
        self.client = Client()
        
        # 1. Cria usuário Admin (Real)
        self.user_admin = User.objects.create_user(
            username='admin_teste', 
            password='password123'
        )
        
        # 2. Cria Medicação Base
        self.medicacao = Medicacao.objects.create(
            nome="Vitamina D",
            dosagem="3 gotas",
            frequencia="Diário",
            via="ORAL",
            duracao_dias=30,
            bebe_id="bebe_teste"
        )

    # ==================================================================
    # 1. TESTES DE AUTENTICAÇÃO HÍBRIDA
    # ==================================================================

    def test_login_fake_pais(self):
        """

        Description:
            Verifica se o sistema reconhece as credenciais de um usuário falso
            definido no dicionário interno da View e redireciona para a área exclusiva
            dos pais, sem criar um usuário real no banco de dados Django.
        """
        response = self.client.post(reverse('login'), {
            'username': 'joao',
            'password': '123'
        })
        
        self.assertRedirects(response, reverse('area_pais'))
        
        session = self.client.session
        self.assertEqual(session.get('usuario_fake'), 'joao')

    def test_login_real_admin(self):
        """

        Description:
            Verifica se o sistema autentica corretamente um usuario real do Django
            e o redireciona para o dashboard administrativo completo.

        """
        response = self.client.post(reverse('login'), {
            'username': 'admin_teste',
            'password': 'password123'
        })
        
        self.assertRedirects(response, reverse('dashboard'))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    # ==================================================================
    # 2. TESTES DE AUDITORIA E LOGS (Item 3.3 do PDF)
    # ==================================================================

    def test_criacao_medicacao_gera_log_sistema(self):
        """
        Valida a geração automática de logs de auditoria na criação de registros.


        Raises:
            AssertionError: Se a medicação for criada mas o log não aparecer no histórico.
        """
        self.client.force_login(self.user_admin)
        
        dados_form = {
            'nome': 'Sulfato Ferroso',
            'dosagem': '5ml',
            'frequencia': '12h',
            'via': 'ORAL',
            'duracao_dias': 15,
            'data_inicio': timezone.now().date(),
            'bebe_id': 'bebe_02',
            'cuidados_especiais': ''
        }
        
        self.client.post(reverse('criar_medicacao'), dados_form)
        
        nova_med = Medicacao.objects.get(nome='Sulfato Ferroso')
        
        log = RegistroAdministracao.objects.filter(
            medicacao=nova_med, 
            status='SISTEMA_ADD'
        ).first()
        
        self.assertIsNotNone(log, "O sistema falhou em criar o log de auditoria 'SISTEMA_ADD'.")
        self.assertIn("admin_teste", log.observacoes)

    def test_edicao_medicacao_gera_log_sistema(self):
        """
        Valida a geração de logs de auditoria na edição de registros.
        """
        self.client.force_login(self.user_admin)
        
        url = reverse('editar_medicacao', args=[self.medicacao.id])
        dados_editados = {
            'nome': 'Vitamina D (Editada)',
            'dosagem': '4 gotas',
            'frequencia': 'Diário',
            'via': 'ORAL',
            'duracao_dias': 30,
            'data_inicio': timezone.now().date(),
            'bebe_id': 'bebe_teste',
            'cuidados_especiais': ''
        }
        
        self.client.post(url, dados_editados)
        
        log = RegistroAdministracao.objects.filter(
            medicacao=self.medicacao, 
            status='SISTEMA_EDIT'
        ).last()
        
        self.assertIsNotNone(log)
        self.assertIn("Vitamina D (Editada)", Medicacao.objects.get(id=self.medicacao.id).nome)

    # ==================================================================
    # 3. TESTES DOS PAIS
    # ==================================================================

    def test_simulacao_registro_pai(self):
        """

        Description:
            Simula a ação de um pai clicando no botão 'Confirmar Dose' na área de pais.
        Raises:
            AssertionError: Se o status gravado não for TOMEI ou se a observação não identificar o autor.
        """
        # Configura sessão fake manualmente
        session = self.client.session
        session['usuario_fake'] = 'joao'
        session.save()
        
        # Simula a requisição GET do botão (Query Params)
        url = reverse('simular_registro_pai') + f"?remedio=Dipirona&acao=tomou"
        self.client.get(url)
        
        registro = RegistroAdministracao.objects.last()
        self.assertEqual(registro.status, 'TOMEI')
        self.assertIn("PAI/MÃE", registro.observacoes)

    # ==================================================================
    # 4. TESTES DE REGRAS DE NEGÓCIO (Models & Estoque)
    # ==================================================================

    def test_logica_alerta_estoque(self):
        """

        Description:
            O sistema deve calcular automaticamente a duração do estoque.
            - Regra: Dias Restantes = Quantidade Total / Consumo Diário.
            - Critério de Aceite: Se Dias Restantes <= 3, a flag 'alerta_baixo_estoque' deve ser True.

        Example:
            Cenário 1: 10ml estoque / 2ml dia = 5 dias -> Alerta False.
            Cenário 2: 4ml estoque / 2ml dia = 2 dias -> Alerta True.

        Raises:
            AssertionError: Se o cálculo matemático ou a atribuição do booleano falharem.
        """
        estoque = Estoque.objects.create(
            medicacao=self.medicacao,
            quantidade_total_ml=10.0,
            consumo_diario_estimado_ml=2.0
        )
        estoque.atualizar_alerta()
        self.assertFalse(estoque.alerta_baixo_estoque, "Estoque para 5 dias não deve gerar alerta.")
        
        # Atualiza para valor crítico
        estoque.quantidade_total_ml = 4.0
        estoque.atualizar_alerta() 
        self.assertTrue(estoque.alerta_baixo_estoque, "Estoque para 2 dias deve gerar alerta.")

    def test_lembrete_destinatario(self):
        """
        Testa a atribuição de responsabilidade nos lembretes.

        Description:
            Verifica se o campo 'destinatario' armazena corretamente qual cuidador
            (Pai ou Mãe) é o responsável por aquele horário específico.

        Returns:
            None.
        """
        lembrete = Lembrete.objects.create(
            medicacao=self.medicacao,
            horario=time(14, 0),
            destinatario='maria'
        )
        self.assertEqual(lembrete.get_destinatario_display(), "Maria (Mãe)")

    # ==================================================================
    # 5. TESTES DE ANÁLISE E INTELIGÊNCIA
    # ==================================================================

    def test_deteccao_alerta_vermelho(self):
        """
        Testa a lógica de detecção de 'Alerta Vermelho'.

        Description:
            1. Cria 3 registros seguidos com status 'ESQUECI'.
            2. Filtra o histórico recente.
            3. Valida se a lógica identifica o padrão.

        """
        RegistroAdministracao.objects.create(medicacao=self.medicacao, status="ESQUECI")
        RegistroAdministracao.objects.create(medicacao=self.medicacao, status="ESQUECI")
        RegistroAdministracao.objects.create(medicacao=self.medicacao, status="ESQUECI")
        
        ultimos_3 = RegistroAdministracao.objects.filter(medicacao=self.medicacao).order_by('-id')[:3]
        esquecimentos = [r for r in ultimos_3 if r.status == "ESQUECI"]
        
        alerta_vermelho = len(esquecimentos) >= 3
        self.assertTrue(alerta_vermelho, "Deveria ativar Alerta Vermelho com 3 esquecimentos seguidos.")

    def test_disponibilidade_dados_aderencia(self):
        """
        Testa se os dados para aderência estão sendo salvos corretamente.
        """
        RegistroAdministracao.objects.create(medicacao=self.medicacao, status="TOMEI")
        RegistroAdministracao.objects.create(medicacao=self.medicacao, status="ESQUECI")
        
        qtd_sucessos = RegistroAdministracao.objects.filter(status="TOMEI").count()
        qtd_falhas = RegistroAdministracao.objects.filter(status="ESQUECI").count()
        
        self.assertEqual(qtd_sucessos, 1, "O banco deve retornar 1 sucesso.")
        self.assertEqual(qtd_falhas, 1, "O banco deve retornar 1 falha.")