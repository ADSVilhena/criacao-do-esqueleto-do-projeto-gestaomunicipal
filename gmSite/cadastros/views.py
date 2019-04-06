from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import CadastroPessoaForm, CadastroEnderecoForm,CadastroTelefoneForm

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
            return redirect('/cadastros/address')
    else:
        form = CadastroPessoaForm()
        context = {'form': form}
        return render(request,'cadastros/cadastro.html',context)


def cadastrarEndereco(request):
    if request.method == 'POST':
        form = CadastroEnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadastros/phone')
    else:
        form = CadastroEnderecoForm()
        context = {'form': form}
        return render(request,'cadastros/cadastroEndereco.html',context)

def cadastrarTelefone(request):
    if request.method == 'POST':
        form = CadastroTelefoneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadastros/success')
    else:
        form = CadastroTelefoneForm()
        context = {'form': form}
        return render(request,'cadastros/cadastroTelefone.html',context)    