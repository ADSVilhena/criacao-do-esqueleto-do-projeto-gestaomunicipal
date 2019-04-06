from django import forms
from django.contrib.auth.models import User
from .models import Pessoa, Endereco, Telefone

class CadastroPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class CadastroEnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

class CadastroTelefoneForm(forms.ModelForm):
    class Meta:
        model = Telefone
        fields = '__all__'        

class DadosUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'