from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Pessoa

from .forms import CadastroEnderecoForm,CadastroTelefoneForm, DadosUserForm, PessoaUserForm

# View de Cadastros


def index(request):
    return HttpResponse("Cadastros")

def sucesso(request,cpf):
    return render(request,'cadastros/sucesso.html')


def cadastrarPessoaUser(request):
    if request.method == 'POST':
        form = PessoaUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("address/"+request.POST["username"])
        else:
            return HttpResponse("O formulário não é válido")
    else:
        form = PessoaUserForm()
        context = {'form': form}
        return render(request,'cadastros/cadastro.html',context)

def cadastrarEndereco(request,cpf):
    if request.method == 'POST':
        form = CadastroEnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(cadastrarTelefone, cpf)
        else:
            return HttpResponse("O formulário não é válido")
    else:
        form = CadastroEnderecoForm()
        context = {'form': form}
        return render(request,'cadastros/cadastroEndereco.html',context)

def cadastrarTelefone(request,cpf):
    if request.method == 'POST':
        form = CadastroTelefoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(sucesso, cpf)
        else:
            return HttpResponse("O formulário não é válido")
    else:
        form = CadastroTelefoneForm()
        context = {'form': form}
        return render(request,'cadastros/cadastroTelefone.html',context)
