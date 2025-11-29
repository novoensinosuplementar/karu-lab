from django.db import models
from django.contrib.auth.models import User

# ---------- PACIENTES ----------
class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    responsavel = models.ForeignKey(User, on_delete=models.CASCADE)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome


# ---------- MEDICAÇÃO ----------
class Medicacao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


# ---------- PRESCRIÇÃO ----------
class Prescricao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medicacao = models.ForeignKey(Medicacao, on_delete=models.CASCADE)
    dosagem = models.CharField(max_length=100)
    frequencia = models.CharField(max_length=100)
    horario_inicial = models.TimeField()
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.medicacao.nome} para {self.paciente.nome}"


# ---------- ADMINISTRAÇÃO DE MEDICAMENTO ----------
class Administracao(models.Model):
    prescricao = models.ForeignKey(Prescricao, on_delete=models.CASCADE)
    horario_real = models.DateTimeField()
    comentario = models.TextField(blank=True)

    def __str__(self):
        return f"Administração de {self.prescricao.medicacao.nome} em {self.horario_real}"


# ---------- QUESTIONÁRIO ----------
class QuestionCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    frequency = models.CharField(max_length=50)  # semanal, mensal, etc

    def __str__(self):
        return f"{self.name} ({self.frequency})"


class Question(models.Model):
    text = models.TextField()
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:50]

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey("Paciente", on_delete=models.CASCADE) 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.question} - {self.score}"

class Alerta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=20)  # grave, moderado
    media = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Alerta {self.nivel} - {self.question.text[:30]}"
    

class Acompanhamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    descricao = models.TextField()

    def __str__(self):
        return f"Acompanhamento de {self.paciente.nome} em {self.data:%d/%m/%Y}"

