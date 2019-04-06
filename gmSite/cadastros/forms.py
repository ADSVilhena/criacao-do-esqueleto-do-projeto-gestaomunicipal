from django import forms
from .models import Pessoa, Endereco

class CadastroPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class CadastroEnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'