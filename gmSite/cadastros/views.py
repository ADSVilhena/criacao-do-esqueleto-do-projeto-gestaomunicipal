from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import CadastroEnderecoForm,CadastroTelefoneForm, PessoaUserForm, PessoaUserFormUpdate
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
    form_class = PessoaUserFormUpdate
    template_name = "cadastros/cadastro.html"    
    success_url = reverse_lazy('testeHome')


class CriarEndereco(CreateView):
    model = Endereco
    form_class = CadastroEnderecoForm
    template_name = "cadastros/cadastroEndereco.html"
    success_url = reverse_lazy("testeHome")


class AtualizarEndereco(UpdateView):
    model = Endereco
    form_class = CadastroEnderecoForm
    template_name = "cadastros/cadastroEndereco.html"
    success_url = reverse_lazy('testeHome')    


class CriarTelefone(CreateView):
    model = Telefone
    form_class = CadastroTelefoneForm
    template_name = "cadastros/cadastroTelefone.html"
    success_url = reverse_lazy('testeHome')


class AtualizarTelefone(UpdateView):
    model = Telefone
    form_class = CadastroTelefoneForm
    template_name = "cadastros/cadastroTelefone.html"
    success_url = reverse_lazy('testeHome')   


class DeletarTelefone(DeleteView):
    model = Telefone
    template_name = "cadastros/telefone_confirm_delete.html"
    success_url = reverse_lazy('testeHome')


class ListarEnderecos(ListView):
    template_name = "cadastros/enderecos_list.html"
    context_object_name = 'enderecos_list'

    def get_queryset(self):
        self.idPessoa = get_object_or_404(User, id=self.kwargs['pk'])
        return Endereco.objects.filter(idPessoa_id=self.idPessoa)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['idPessoa'] = self.idPessoa
        return context


class ListarTelefones(ListView):
    template_name = "cadastros/telefones_list.html"
    context_object_name = 'telefones_list'

    def get_queryset(self, **kwargs):
        self.idPessoa = get_object_or_404(User, id=self.kwargs['userID'])
        return Telefone.objects.filter(idPessoa_id=self.idPessoa)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['idPessoa'] = self.idPessoa
        return context


