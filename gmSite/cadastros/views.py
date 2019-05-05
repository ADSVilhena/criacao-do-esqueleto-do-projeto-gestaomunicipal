from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import CadastroEnderecoForm,CadastroTelefoneForm, PessoaUserForm, PessoaUserFormUpdate
from .models import Endereco, Telefone, Rua, TipoTelefone

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/?next=%s' % request.path)
    else:
        return HttpResponse("Cadastros")

def sucesso(request):
    return render(request,'cadastros/sucesso.html')

def manterEndereco(request):
    ruas = Rua.objects.all()
    if request.method == 'POST':
        address_form = CadastroEnderecoForm(request.POST)
        if address_form.is_valid():
            address_form.save()
            return render(request, 'cadastros/enderecos_list.html')
        else:
            context = {'address_form': address_form,'ruas': ruas}
            return render(request, 'cadastros/addAddress.html', context)
    else:
        address_form = CadastroEnderecoForm()
        context = {'address_form': address_form,'ruas': ruas}
        return render(request, 'cadastros/addAddress.html', context)

def enderecosList(request):
    enderecos_list = Endereco.objects.filter(idPessoa_id=request.user.id)
    context = {'enderecos_list': enderecos_list}
    return render(request, 'cadastros/listAddress.html', context)

def manterTelefone(request):
    tipos = TipoTelefone.objects.all()
    if request.method == 'POST':
        phone_form = CadastroTelefoneForm(request.POST)
        if phone_form.is_valid():
            phone_form.save()
            return render(request, 'cadastros/telefones_list.html')
        else:
            context = {'phone_form': phone_form,'tipos': tipos}
            return render(request, 'cadastros/addPhone.html', context)
    else:
        phone_form = CadastroEnderecoForm()
        context = {'phone_form': phone_form,'tipos': tipos}
        return render(request, 'cadastros/addPhone.html', context)


def telefonesList(request):
    telefones_list = Telefone.objects.filter(idPessoa_id=request.user.id)
    context = {'telefones_list': telefones_list}
    return render(request, 'cadastros/listPhone.html', context)


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

class DeletarEndereco(DeleteView):
    model = Endereco
    template_name = "cadastros/endereco_confirm_delete.html"
    success_url = reverse_lazy('cadastros:enderecosList')

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
    success_url = reverse_lazy('cadastros:telefonesList')


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


