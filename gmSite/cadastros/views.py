from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import CadastroEnderecoForm,CadastroTelefoneForm, PessoaUserForm
from .models import Endereco, Telefone

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        return HttpResponse("Cadastros")

def sucesso(request):
    return render(request,'cadastros/sucesso.html')


class ListarCadastro(ListView):
    model = User
    context_object_name = 'usuario'


class CriarCadastro(CreateView):
    model = User
    form_class = PessoaUserForm
    template_name = "cadastros/cadastro.html"
    success_url = reverse_lazy('login')


class AtualizarCadastro(UpdateView):
    model = User
    form_class = PessoaUserForm
    template_name = "cadastros/cadastro.html"    
    success_url = reverse_lazy('home')


class CriarEndereco(CreateView):
    model = Endereco
    form_class = CadastroEnderecoForm
    template_name = "cadastros/cadastroEndereco.html"
    success_url = reverse_lazy('cadastros:telefone')


class AtualizarEndereco(UpdateView):
    model = Endereco
    form_class = CadastroEnderecoForm
    template_name = "cadastros/cadastroEndereco.html"
    success_url = reverse_lazy('cadastros:sucesso')    


class CriarTelefone(CreateView):
    model = Telefone
    form_class = CadastroTelefoneForm
    template_name = "cadastros/cadastroTelefone.html"
    success_url = reverse_lazy('cadastros:sucesso')


class AtualizarTelefone(UpdateView):
    model = Telefone
    form_class = CadastroTelefoneForm
    template_name = "cadastros/cadastroTelefone.html"
    success_url = reverse_lazy('cadastros:sucesso')   


class ListarEnderecos(ListView):
    template_name = "cadastros/enderecos_list.html"
    context_object_name = 'enderecos_list'

    def get_queryset(self):
        return Endereco.objects.filter(idPessoa_id=1)