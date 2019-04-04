from django import forms

class NameForm(forms.Form):
    nome = forms.CharField(label='PESSOA',max_length=150)
    cpf = forms.CharField(label='CPF',max_length=11)
    senha = forms.CharField(label='SENHA',max_length=11)
    email = forms.EmailField(label='E-MAIL',max_length=100)
