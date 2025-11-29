import datetime
from .models import Answer, Question

# Média de respostas dentro de um intervalo (em dias)
def media_periodo(user, question, dias):
    hoje = datetime.date.today()
    inicio = hoje - datetime.timedelta(days=dias)

    respostas = Answer.objects.filter(
        user=user,
        question=question,
        date__gte=inicio
    )

    if not respostas.exists():
        return None  # ainda não tem dados suficientes

    soma = sum(r.score for r in respostas)
    media = soma / respostas.count()
    return media


def checar_alerta(user, question):
    categoria = question.category.frequency.lower()

    if categoria == "semanal":
        media = media_periodo(user, question, 30)  # 1 mês
    elif categoria == "mensal":
        media = media_periodo(user, question, 60)  # 2 meses
    else:
        return False  # categorias que não exigem alerta

    if media is not None and media < 3:
        return True

    return False