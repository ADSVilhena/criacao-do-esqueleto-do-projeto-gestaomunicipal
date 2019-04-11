from django import forms
from .models import Chamados

class ChamadosForm(forms.ModelForm):
    class Meta:
        model = Chamados
        fields = '__all__'
