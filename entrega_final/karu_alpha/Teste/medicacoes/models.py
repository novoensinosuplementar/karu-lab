from django.db import models
from django.utils import timezone

class Medicacao(models.Model):
    VIA_ADMINISTRACAO = [
        ("ORAL", "Oral"),
        ("IM", "Intramuscular"),
    ]

    nome = models.CharField(max_length=150)
    dosagem = models.CharField(max_length=100)
    frequencia = models.CharField(max_length=100)
    via = models.CharField(max_length=10, choices=VIA_ADMINISTRACAO)
    duracao_dias = models.IntegerField()
    data_inicio = models.DateField(default=timezone.now)
    cuidados_especiais = models.TextField(blank=True)
    bebe_id = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} ({self.bebe_id})"

class Lembrete(models.Model):
    # --- NOVO: OPÇÕES DE USUÁRIOS ---
    USUARIOS_ALVO = [
        ('joao', 'João (Pai)'),
        ('maria', 'Maria (Mãe)'),
    ]

    medicacao = models.ForeignKey(Medicacao, on_delete=models.CASCADE, related_name="lembretes")
    horario = models.TimeField()
    canal_preferido = models.CharField(max_length=20, default="APP")
    tolerancia_minutos = models.IntegerField(default=30)
    
    # --- NOVO CAMPO: DESTINATÁRIO ---
    destinatario = models.CharField(
        max_length=20, 
        choices=USUARIOS_ALVO, 
        default='joao',
        verbose_name="Responsável"
    )

    def __str__(self):
        return f"Lembrete para {self.get_destinatario_display()} - {self.medicacao.nome}"

class Estoque(models.Model):
    medicacao = models.OneToOneField(Medicacao, on_delete=models.CASCADE, related_name="estoque")
    quantidade_total_ml = models.FloatField()
    consumo_diario_estimado_ml = models.FloatField()
    alerta_baixo_estoque = models.BooleanField(default=False)

    def atualizar_alerta(self):
        if self.consumo_diario_estimado_ml > 0:
            dias_restantes = self.quantidade_total_ml / self.consumo_diario_estimado_ml
            self.alerta_baixo_estoque = dias_restantes <= 3
        else:
            self.alerta_baixo_estoque = False
        self.save()

    def __str__(self):
        return f"Estoque de {self.medicacao.nome}"

class RegistroAdministracao(models.Model):
    OPCOES = [
        ("TOMEI", "Tomei/Dei a medicação"),
        ("ESQUECI", "Esqueci"),
        ("RECUSEI", "Bebê recusou"),
        ("VOMITOU", "Vomitou após tomar"),
        ("SISTEMA_ADD", "✨ Cadastro Novo"),
        ("SISTEMA_EDIT", "✏️ Edição de Dados"),
        ("ESTOQUE_UP", "📦 Atualização de Estoque"),
    ]

    medicacao = models.ForeignKey(Medicacao, on_delete=models.CASCADE, related_name="registros")
    horario_registro = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=OPCOES)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.medicacao.nome} - {self.status}"
        