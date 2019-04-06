from django import forms
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
