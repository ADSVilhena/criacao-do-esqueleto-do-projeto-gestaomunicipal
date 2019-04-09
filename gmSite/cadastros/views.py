from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import Pessoa

from .forms import CadastroPessoaForm, CadastroEnderecoForm,CadastroTelefoneForm, DadosUserForm, PessoaUserForm

# View de Cadastros


def index(request):
    return HttpResponse("Cadastros")

def sucesso(request):
    return render(request,'cadastros/sucesso.html')


def cadastrar(request):
    if request.method == 'POST':
        form = CadastroPessoaForm(request.POST)
        if form.is_valid():
            form.save()
            pessoa_salva = Pessoa.objects.get(cpf=request.POST.get('cpf'))
            return redirect('/cadastros/address/' + str(pessoa_salva.id) + '/')
    else:
        form = CadastroPessoaForm()
        context = {'form': form}
        return render(request,'cadastros/cadastro.html',context)


def cadastrarPessoaUser(request):
    if request.method == 'POST':
        form = PessoaUserForm(request.POST)
        if form.is_valid():
            form.save()
            pessoa_salva = User.objects.get(username=request.POST.get('username'))
            return redirect('/cadastros/address/' + str(pessoa_salva.id) + '/')
    else:
        form = PessoaUserForm()
        context = {'form': form}
        return render(request,'cadastros/cadastro.html',context)

def cadastrarEndereco(request, pessoa_id):
    pessoa = get_object_or_404(Pessoa, pk=pessoa_id)
    if request.method == 'POST':
        form = CadastroEnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadastros/phone')
    else:
        form = CadastroEnderecoForm()
        form.numero = pessoa_id
        context = {'form': form}
        return render(request,'cadastros/cadastroEndereco.html',context)

def cadastrarTelefone(request, pessoa_id):
    if request.method == 'POST':
        form = CadastroTelefoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadastros/success')
    else:
        form = CadastroTelefoneForm()
        context = {'form': form}
        return render(request,'cadastros/cadastroTelefone.html',context)    

def dadosUsuario(request):
    if request.method == 'POST':
        form = DadosUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadastros/success')
    else:
        form = DadosUserForm()
        context = {'form': form}
        return render(request,'cadastros/user.html',context)     