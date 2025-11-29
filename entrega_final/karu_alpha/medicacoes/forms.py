from django import forms
from .models import Medicacao, Lembrete, Estoque, RegistroAdministracao

class MedicacaoForm(forms.ModelForm):
    class Meta:
        model = Medicacao
        fields = '__all__'
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}),
            'cuidados_especiais': forms.Textarea(attrs={'rows': 3}),
        }

class LembreteForm(forms.ModelForm):
    class Meta:
        model = Lembrete
        # ADICIONADO: 'destinatario' na lista de campos
        fields = ['medicacao', 'destinatario', 'horario', 'canal_preferido', 'tolerancia_minutos']
        widgets = {
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['medicacao', 'quantidade_total_ml', 'consumo_diario_estimado_ml']

class RegistroForm(forms.ModelForm):
    class Meta:
        model = RegistroAdministracao
        fields = ['medicacao', 'status', 'observacoes']
        widgets = {
            'observacoes': forms.Textarea(attrs={'rows': 2}),
        }
        