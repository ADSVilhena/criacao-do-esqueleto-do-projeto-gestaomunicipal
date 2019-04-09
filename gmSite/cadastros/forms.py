from django import forms
from django.contrib.auth.models import User
from .models import Pessoa, Endereco, Telefone

class CadastroPessoaForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = ('id', 'nome', 'cpf', 'email', 'senha')

class PessoaUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password',)
        labels = {'username':'CPF'}

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