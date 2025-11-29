'''from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, timedelta
from .models import Question, Answer, QuestionCategory, Paciente
from .utils import checar_alerta

# ---------------- HOME ----------------
def home(request):
    #return render(request, 'base.html')
    return render(request, 'dashboard_gestao.html')

def dashboard_gestao(request):

    #total_acompanhamentos = 10

    return render(request, 'dashboard_gestao.html')

def questionario_lista(request):    
    questionarios = QuestionCategory.objects.all()
    return render(request, 'questionario_lista.html', {
        'questionarios': questionarios
    })

@login_required
def questionario_responder(request, pk):
    questionario = get_object_or_404(QuestionCategory, pk=pk)

    # Lista de perguntas da categoria
    perguntas_qs = Question.objects.filter(category=questionario).order_by('id')

    # Pega o paciente: você disse que é sempre o ID 1
    paciente = get_object_or_404(Paciente, id=1)

    # Respostas prévias do usuário para esta categoria
    respostas = Answer.objects.filter(
        user=request.user, 
        paciente=paciente,
        question__in=perguntas_qs
    )

    respostas_by_qid = {a.question_id: a for a in respostas}

    # Anexa answer_user em cada pergunta (para o template preencher)
    perguntas = []
    for p in perguntas_qs:
        p.answer_user = respostas_by_qid.get(p.id)  # pode ser None
        perguntas.append(p)

    # ----------------------------
    # PROCESSAMENTO DO POST
    # ----------------------------
    if request.method == 'POST':
        for p in perguntas:
            score_key = f"score_{p.id}"
            obs_key = f"obs_{p.id}"

            score_val = request.POST.get(score_key)
            comment_val = request.POST.get(obs_key, "").strip()

            if score_val is None:
                continue

            try:
                score_val = int(score_val)
            except ValueError:
                continue

            # Verifica se existe resposta
            answer_obj = Answer.objects.filter(
                user=request.user,
                paciente=paciente,
                question=p
            ).first()

            if answer_obj:
                # UPDATE
                answer_obj.score = score_val
                answer_obj.comment = comment_val
                answer_obj.save()
            else:
                # CREATE
                Answer.objects.create(
                    user=request.user,
                    paciente=paciente,
                    question=p,
                    score=score_val,
                    comment=comment_val
                )

        messages.success(request, "Respostas salvas com sucesso!")
        return redirect("questionario_lista")

    # ----------------------------
    # GET — mostrar formulário
    # ----------------------------
    context = {
        "questionario": questionario,
        "perguntas": perguntas,
        "form": None,
    }
    return render(request, "questionario_responder.html", context)


# ---------------- QUESTIONÁRIO ----------------
@login_required
def questionario(request):

    perguntas = Question.objects.all().order_by("category__name")

    if request.method == "POST":

        for pergunta in perguntas:
            score = request.POST.get(f"score_{pergunta.id}")
            comment = request.POST.get(f"comment_{pergunta.id}")

            if score is not None:

                Answer.objects.create(
                    user=request.user,
                    question=pergunta,
                    score=int(score),
                    comment=comment
                )

        messages.success(request, "Respostas enviadas com sucesso!")
        return redirect("questionario")

    return render(request, "questionarios/questionario.html", {"perguntas": perguntas})




# ---------------- CÁLCULO DE MÉDIA POR PERÍODO ----------------
def media_periodo(user, question, dias):

    hoje = date.today()
    inicio = hoje - timedelta(days=dias)

    respostas = Answer.objects.filter(
        user=user,
        question=question,
        date__gte=inicio
    )

    # Se não completou o período mínimo → NÃO calcula alerta
    if not respostas.exists():
        return None  

    soma = sum(r.score for r in respostas)
    return soma / respostas.count()


# ---------------- ALERTAS (VERSÃO FINAL) ----------------
@login_required
def alertas(request):

    perguntas = Question.objects.all().order_by("category__name")
    alertas = []

    hoje = date.today()

    for pergunta in perguntas:

        freq = pergunta.category.frequency.lower()

        # ---- Determina o período correto ----
        if "seman" in freq:
            dias = 7      # mês completo
        elif "quinzen" in freq:
            dias = 15
        elif "mensal" in freq:
            dias = 30      # 2 meses
        else:
            dias = 30

        # ---- Pega a última resposta do usuário ----
        ultima = Answer.objects.filter(
            user=request.user,
            question=pergunta
        ).order_by('-date').first()

        # Se nunca respondeu → não mostra nada
        if not ultima:
            continue

        # Verifica se já passou o período mínimo
        dias_passados = (hoje - ultima.date).days

        if dias_passados < dias:
            # Ainda não completou o ciclo → não calcula média
            continue

        # ---- Calcula média do período ----
        media = media_periodo(request.user, pergunta, dias)

        if media is not None and media < 3:
            alertas.append({
                "pergunta": pergunta.text,
                "categoria": pergunta.category.name,
                "frequencia": pergunta.category.frequency,
                "media": round(media, 2),
                "periodo_dias": dias,
                "ultima_data": ultima.date
            })

    return render(request, "templates/questionarios/alertas.html", {
        "alertas": alertas
    })




def acompanhamentos(request):
    return render(request, 'acompanhamentos.html')

def listar_alertas(request):
    return render(request, 'listar_alertas.html')





from django.shortcuts import render
from .models import Acompanhamento  # ajuste para o nome correto do model

def acompanhamentos_lista(request):
    acompanhamentos = Acompanhamento.objects.all().order_by('-data')
    return render(request, 'lista.html', {
        'acompanhamentos': acompanhamentos
    })


#------------------------------------------------------------------------------


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Acompanhamento, Paciente  # ajuste se necessário

def acompanhamento_novo(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        descricao = request.POST.get('descricao')

        paciente = Paciente.objects.get(id=paciente_id)

        Acompanhamento.objects.create(
            paciente=paciente,
            descricao=descricao
        )

        messages.success(request, "Acompanhamento registrado com sucesso!")
        return redirect('acompanhamentos_lista')

    pacientes = Paciente.objects.all()

    return render(request, 'acompanhamentos.html', {
        'pacientes': pacientes
    })'''




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date, timedelta
from .models import Question, Answer, QuestionCategory, Paciente
from .utils import checar_alerta

# ---------------- HOME ----------------
def home(request):
    #return render(request, 'base.html')
    return render(request, 'dashboard_gestao.html')

from .models import Answer, Paciente

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Answer, Paciente, Acompanhamento, Alerta
from django.db.models import Q

@login_required
def dashboard_gestao(request):

    # Paciente fixo por enquanto
    paciente = Paciente.objects.get(id=1)

    # ----- TOTAL DE ACOMPANHAMENTOS -----
    total_acompanhamentos = Acompanhamento.objects.filter(paciente=paciente).count()

    # ----- TOTAL DE ALERTAS -----
    total_alertas = Alerta.objects.filter(user=request.user).count()

    # ----- ALERTAS CRÍTICOS (não vistos) -----
    alertas_criticos = Alerta.objects.filter(
        user=request.user,
        nivel='CRITICO'
    ).count()

    # ----- TAXA DE CONCLUSÃO (fake por enquanto, até criar tasks) -----
    taxa_conclusao = 0

    # ----- ATIVIDADE RECENTE (últimas 60 respostas) -----
    respostas_recentes = Answer.objects.filter(
        paciente=paciente
    ).order_by('-date')[:60]

    return render(request, 'dashboard_gestao.html', {
        "total_acompanhamentos": total_acompanhamentos,
        "total_alertas": total_alertas,
        "alertas_criticos": alertas_criticos,
        "taxa_conclusao": taxa_conclusao,
        "respostas_recentes": respostas_recentes,
    })
def questionario_lista(request):    
    questionarios = QuestionCategory.objects.all()
    return render(request, 'questionario_lista.html', {
        'questionarios': questionarios
    })

@login_required
def questionario_responder(request, pk):
    questionario = get_object_or_404(QuestionCategory, pk=pk)

    # Lista de perguntas da categoria
    perguntas = Question.objects.filter(category=questionario).order_by('id')

    # Paciente fixo (como você usa atualmente)
    paciente = get_object_or_404(Paciente, id=1)

    if request.method == 'POST':
        for p in perguntas:
            score_key = f"score_{p.id}"
            obs_key = f"obs_{p.id}"

            score_val = request.POST.get(score_key)
            comment_val = request.POST.get(obs_key, "").strip()

            if not score_val:
                continue

            try:
                score_val = int(score_val)
            except ValueError:
                continue

            # 👉 SEM UPDATE — sempre cria uma nova resposta
            Answer.objects.create(
                user=request.user,
                paciente=paciente,
                question=p,
                score=score_val,
                comment=comment_val
            )

        messages.success(request, "Respostas enviadas!")
        return redirect("questionario_lista")

    return render(request, "questionario_responder.html", {
        "questionario": questionario,
        "perguntas": perguntas
    })
    # ----------------------------
    # GET — mostrar formulário
    # ----------------------------
    context = {
        "questionario": questionario,
        "perguntas": perguntas,
        "form": None,
    }
    return render(request, "questionario_responder.html", context)


# ---------------- QUESTIONÁRIO ----------------
@login_required
def questionario(request):

    perguntas = Question.objects.all().order_by("category__name")

    paciente = Paciente.objects.get(id=1)  # ADICIONE ISSO

    if request.method == "POST":

        for pergunta in perguntas:
            score = request.POST.get(f"score_{pergunta.id}")
            comment = request.POST.get(f"comment_{pergunta.id}")

            if score is not None:

                Answer.objects.create(
                    user=request.user,
                    paciente=paciente,     # ADICIONE ESTA LINHA
                    question=pergunta,
                    score=int(score),
                    comment=comment
                )

        messages.success(request, "Respostas enviadas com sucesso!")
        return redirect("questionario")

    return render(request, "questionarios/questionario.html", {"perguntas": perguntas})

# ---------------- CÁLCULO DE MÉDIA POR PERÍODO ----------------
def media_periodo(user, question, dias):

    hoje = date.today()
    inicio = hoje - timedelta(days=dias)

    respostas = Answer.objects.filter(
        user=user,
        question=question,
        date__gte=inicio
    )

    # Se não completou o período mínimo → NÃO calcula alerta
    if not respostas.exists():
        return None  

    soma = sum(r.score for r in respostas)
    return soma / respostas.count()


# ---------------- ALERTAS (VERSÃO FINAL) ----------------
@login_required
def alertas(request):

    perguntas = Question.objects.all().order_by("category__name")
    alertas = []

    hoje = date.today()

    for pergunta in perguntas:

        freq = pergunta.category.frequency.lower()

        # ---- Determina o período correto ----
        if "seman" in freq:
            dias = 30      # mês completo
        elif "quinzen" in freq:
            dias = 45
        elif "mensal" in freq:
            dias = 60      # 2 meses
        else:
            dias = 30

        # ---- Pega a última resposta do usuário ----
        ultima = Answer.objects.filter(
            user=request.user,
            question=pergunta
        ).order_by('-date').first()

        # Se nunca respondeu → não mostra nada
        if not ultima:
            continue

        # Verifica se já passou o período mínimo
        dias_passados = (hoje - ultima.date).days

        if dias_passados < dias:
            # Ainda não completou o ciclo → não calcula média
            continue

        # ---- Calcula média do período ----
        media = media_periodo(request.user, pergunta, dias)

        if media is not None and media < 3:
            alertas.append({
                "pergunta": pergunta.text,
                "categoria": pergunta.category.name,
                "frequencia": pergunta.category.frequency,
                "media": round(media, 2),
                "periodo_dias": dias,
                "ultima_data": ultima.date
            })

    return render(request, "questionarios/alertas.html", {
        "alertas": alertas
    })


def acompanhamentos(request):
    return render(request, 'acompanhamentos.html')

def listar_alertas(request):
    return render(request, 'listar_alertas.html')