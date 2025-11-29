from django.test import TestCase
from django.contrib.auth.models import User
from .models import Paciente, QuestionCategory, Question, Answer, Alerta
from datetime import date

class SimpleQuestionnaireTest(TestCase):
    def setUp(self):
        # Usuário de teste
        self.user = User.objects.create_user(username="testuser", password="12345")

        # Paciente fake para satisfazer a constraint NOT NULL
        self.paciente = Paciente.objects.create(
            nome="Paciente Teste",
            data_nascimento=date(2000, 1, 1),
            responsavel=self.user
        )

        # Categoria de questionário
        self.category = QuestionCategory.objects.create(
            name="Saúde Geral",
            description="Perguntas sobre saúde",
            frequency="semanal"
        )

        # Pergunta
        self.question = Question.objects.create(
            text="Como você está se sentindo hoje?",
            category=self.category
        )

        # Resposta
        self.answer = Answer.objects.create(
            user=self.user,
            paciente=self.paciente,  # paciente obrigatório
            question=self.question,
            score=5,
            comment="Tudo bem"
        )

        # Alerta
        self.alerta = Alerta.objects.create(
            user=self.user,
            question=self.question,
            nivel="moderado",
            media=4.5
        )

    def test_questioncategory_creation(self):
        self.assertIn("Saúde Geral", str(self.category))

    def test_question_creation(self):
        self.assertIn("Como você está se sentindo", str(self.question))

    def test_answer_creation(self):
        self.assertEqual(self.answer.score, 5)
        self.assertEqual(self.answer.comment, "Tudo bem")
        self.assertIn("Como você está se sentindo hoje?", str(self.answer))


    def test_alerta_creation(self):
        self.assertIn("Alerta moderado", str(self.alerta))

