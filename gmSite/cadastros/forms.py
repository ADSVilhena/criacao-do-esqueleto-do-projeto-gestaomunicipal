from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Endereco, Telefone


class PessoaUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password1', 'password2')
        labels = {'username':'CPF'}


class CadastroEnderecoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CadastroEnderecoForm, self).__init__(*args, **kwargs)
       #self.fields['idRua'].widget.attrs = {'class':'form-group form-control', 'type':'text', 'placeholder':'idRua'}
        self.fields['numero'].widget.attrs = {'class':'forms''form-group form-control', 'type':'text', 'placeholder':'numero da Rua'}
        self.fields['complemento'].widget.attrs = {'class':'form-group form-control', 'type':'text', 'placeholder':'complemento'}
        #self.fields['idPessoa'].widget.attrs = {'class':'form-group form-control', 'type':'text'}

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