from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['score', 'comment']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 0, 'max': 5}),
            'comment': forms.Textarea(attrs={'rows': 2}),
        }