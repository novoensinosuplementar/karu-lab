from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Medicacao, Lembrete, Estoque, RegistroAdministracao
from .forms import MedicacaoForm, LembreteForm, EstoqueForm, RegistroForm

# === DADOS MOCKUP (Fakes) ===
USUARIOS_FAKE = {
    "joao": {
        "senha": "123",
        "nome_exibicao": "João (Pai)",
        "remedios": [
            {"nome": "Dipirona", "dosagem": "15 gotas", "horario": "08:00"},
            {"nome": "Vitamina C", "dosagem": "1 comprimido", "horario": "10:00"}
        ]
    },
    "maria": {
        "senha": "abc",
        "nome_exibicao": "Maria (Mãe)",
        "remedios": [
            {"nome": "Insulina", "dosagem": "2 unidades", "horario": "12:00"},
            {"nome": "Omeprazol", "dosagem": "1 cápsula", "horario": "07:00"}
        ]
    }
}

# === LOGIN HÍBRIDO (CORRIGIDO) ===
def login_view(request):
    if request.method == 'POST':
        usuario_form = request.POST.get('username')
        senha_form = request.POST.get('password')

        # 1. Tenta primeiro como Usuário Fake (Prioridade para a Demo)
        if usuario_form in USUARIOS_FAKE and senha_form == USUARIOS_FAKE[usuario_form]['senha']:
            request.session['usuario_fake'] = usuario_form
            return redirect('area_pais')
        
        # 2. Se não for fake (ou senha errada), tenta autenticação Real do Django (Admin)
        user = authenticate(request, username=usuario_form, password=senha_form)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard') # Vai para o sistema real (Admin)
        else:
            messages.error(request, 'Usuário ou senha incorretos.')

    return render(request, 'registration/login.html')

def logout_view(request):
    # 1. Pega o sistema de mensagens
    storage = messages.get_messages(request)
    
    # 2. "Lê" todas as mensagens pendentes para forçar a limpeza delas
    for _ in storage:
        pass 
    
    logout(request) # Logout do Django
    request.session.flush() # Limpa sessão fake
    return redirect('login')

# === ÁREA DOS PAIS (MOCKUP) ===
def area_pais(request):
    usuario_key = request.session.get('usuario_fake')
    
    if not usuario_key or usuario_key not in USUARIOS_FAKE:
        return redirect('login')

    dados_usuario = USUARIOS_FAKE[usuario_key]
    
    # NOVO: Buscar lembretes reais do banco de dados filtrados por destinatário
    lembretes_reais = Lembrete.objects.filter(destinatario=usuario_key).order_by('horario')
    
    return render(request, 'medicacoes/dashboard_pais.html', {
        'usuario': dados_usuario,
        'remedios': dados_usuario['remedios'],
        'lembretes': lembretes_reais  # Novo: passar lembretes reais do banco
    })

def simular_registro_pai(request):
    usuario_key = request.session.get('usuario_fake')
    remedio_nome = request.GET.get('remedio')
    acao = request.GET.get('acao')

    if usuario_key and remedio_nome:
        med_real = Medicacao.objects.first() 
        
        if med_real:
            # Lógica visual melhorada para o feedback
            if acao == 'editou':
                status_code = 'SISTEMA_EDIT'
                # Mensagem técnica para o Histórico do Admin
                msg_admin = f"PAI/MÃE ({USUARIOS_FAKE[usuario_key]['nome_exibicao']}) alterou configurações de: {remedio_nome}"
                # Mensagem amigável para o Pai
                msg_pai = f"Você editou as informações de {remedio_nome} com sucesso!"
            else:
                status_code = 'TOMEI'
                msg_admin = f"PAI/MÃE ({USUARIOS_FAKE[usuario_key]['nome_exibicao']}) registrou dose tomada: {remedio_nome}"
                msg_pai = f"Dose de {remedio_nome} confirmada!"

            RegistroAdministracao.objects.create(
                medicacao=med_real,
                status=status_code,
                observacoes=msg_admin
            )
            messages.success(request, msg_pai)
    
    return redirect('area_pais')


# === SISTEMA REAL (ADMIN) ===

@login_required
def dashboard(request):
    context = {
        'total_medicacoes': Medicacao.objects.count(),
        'total_lembretes': Lembrete.objects.count(),
        'baixo_estoque': Estoque.objects.filter(alerta_baixo_estoque=True).count(),
    }
    return render(request, "dashboard.html", context)

@login_required
def listar_medicacoes(request):
    medicacoes = Medicacao.objects.all().order_by('-data_inicio')
    return render(request, "medicacoes/listar.html", {'medicacoes': medicacoes})

@login_required
def criar_medicacao(request):
    if request.method == 'POST':
        form = MedicacaoForm(request.POST)
        if form.is_valid():
            medicacao = form.save()
            RegistroAdministracao.objects.create(
                medicacao=medicacao,
                status='SISTEMA_ADD',
                observacoes=f"Nova medicação cadastrada por {request.user.username}"
            )
            messages.success(request, 'Medicação criada com sucesso!')
            return redirect('listar_medicacoes')
    else:
        form = MedicacaoForm()
    return render(request, "medicacoes/form.html", {'form': form, 'titulo': 'Nova Medicação'})

@login_required
def editar_medicacao(request, id):
    medicacao = get_object_or_404(Medicacao, id=id)
    if request.method == 'POST':
        form = MedicacaoForm(request.POST, instance=medicacao)
        if form.is_valid():
            form.save()
            RegistroAdministracao.objects.create(
                medicacao=medicacao,
                status='SISTEMA_EDIT',
                observacoes=f"Dados alterados por {request.user.username}"
            )
            messages.success(request, 'Medicação atualizada!')
            return redirect('listar_medicacoes')
    else:
        form = MedicacaoForm(instance=medicacao)
    return render(request, "medicacoes/form.html", {'form': form, 'titulo': f'Editar {medicacao.nome}'})

@login_required
def listar_lembretes(request):
    lembretes = Lembrete.objects.all().order_by('horario')
    return render(request, "lembretes/listar.html", {'lembretes': lembretes})

@login_required
def criar_lembrete(request):
    if request.method == 'POST':
        form = LembreteForm(request.POST)
        if form.is_valid():
            lembrete = form.save()
            RegistroAdministracao.objects.create(
                medicacao=lembrete.medicacao,
                status='SISTEMA_ADD',
                observacoes=f"Novo lembrete definido para {lembrete.horario}"
            )
            messages.success(request, 'Lembrete criado!')
            return redirect('listar_lembretes')
    else:
        form = LembreteForm()
    return render(request, "medicacoes/form.html", {'form': form, 'titulo': 'Novo Lembrete'})

@login_required
def editar_lembrete(request, id):
    lembrete = get_object_or_404(Lembrete, id=id)
    if request.method == 'POST':
        form = LembreteForm(request.POST, instance=lembrete)
        if form.is_valid():
            form.save()
            RegistroAdministracao.objects.create(
                medicacao=lembrete.medicacao,
                status='SISTEMA_EDIT',
                observacoes=f"Horário do lembrete alterado para {lembrete.horario}"
            )
            messages.success(request, 'Lembrete atualizado!')
            return redirect('listar_lembretes')
    else:
        form = LembreteForm(instance=lembrete)
    return render(request, "medicacoes/form.html", {'form': form, 'titulo': 'Editar Lembrete'})

@login_required
def listar_estoque(request):
    estoques = Estoque.objects.all()
    for item in estoques:
        item.atualizar_alerta()
    return render(request, "estoques/listar.html", {'estoques': estoques})

@login_required
def criar_estoque(request):
    if request.method == 'POST':
        form = EstoqueForm(request.POST)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.atualizar_alerta()
            estoque.save()
            RegistroAdministracao.objects.create(
                medicacao=estoque.medicacao,
                status='ESTOQUE_UP',
                observacoes=f"Estoque iniciado: {estoque.quantidade_total_ml}ml"
            )
            messages.success(request, 'Item adicionado ao estoque!')
            return redirect('listar_estoque')
    else:
        form = EstoqueForm()
    return render(request, "medicacoes/form.html", {'form': form, 'titulo': 'Novo Item de Estoque'})

@login_required
def editar_estoque(request, id):
    item = get_object_or_404(Estoque, id=id)
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=item)
        if form.is_valid():
            estoque = form.save(commit=False)
            estoque.atualizar_alerta()
            estoque.save()
            RegistroAdministracao.objects.create(
                medicacao=estoque.medicacao,
                status='ESTOQUE_UP',
                observacoes=f"Estoque atualizado para: {estoque.quantidade_total_ml}ml"
            )
            messages.success(request, 'Estoque atualizado!')
            return redirect('listar_estoque')
    else:
        form = EstoqueForm(instance=item)
    return render(request, "medicacoes/form.html", {'form': form, 'titulo': f'Editar Estoque: {item.medicacao.nome}'})

@login_required
def listar_registros(request):
    registros = RegistroAdministracao.objects.all().order_by('-horario_registro')
    return render(request, "registros/listar.html", {'registros': registros})
