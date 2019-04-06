from django.shortcuts import render, redirect
from django.http import HttpResponse


from .forms import CadastroPessoaForm,CadastroEnderecoForm

# View de Cadastros


def index(request):
    return HttpResponse("Cadastros")


def cadastrar(request):
    if request.method == 'POST':
        form = CadastroPessoaForm(request.POST)
        if form.is_valid():
            form.save()
            formEndereco = CadastroEnderecoForm()
            context = {'form': formEndereco}
            return render(request, 'cadastros/cadastroEndereco.html',context)
    else:
        form = CadastroPessoaForm()
        context = {'form': form}
        return render(request,'cadastros/cadastro.html',context)


def cadastrarEndereco(request):
    if request.method == 'POST':
        form = CadastroEnderecoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Chegou aqui")
        else:
            return HttpResponse("Deu erro aqui")
    else:
        form = CadastroEnderecoForm()
        context = {'form': form}
        return render(request,'cadastros/cadastroEndereco.html',context)