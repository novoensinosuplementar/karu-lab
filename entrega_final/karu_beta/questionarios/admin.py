from django.contrib import admin
from .models import (
    Paciente,
    Medicacao,
    Prescricao,
    Administracao,
    QuestionCategory,
    Question,
    Answer,
)

# Cadastro no admin
admin.site.register(Paciente)
admin.site.register(Medicacao)
admin.site.register(Prescricao)
admin.site.register(Administracao)

# Parte do questionário
admin.site.register(QuestionCategory)
admin.site.register(Question)
admin.site.register(Answer)