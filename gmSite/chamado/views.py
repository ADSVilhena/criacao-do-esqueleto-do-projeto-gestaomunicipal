from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Chamados, Status, Eventos, Endereco
from .forms import ChamadosForm


class ListarChamados(ListView):
    template_name = "chamado/chamados_list.html"
    context_object_name = 'chamados_list'

    def get_queryset(self):
        self.idPessoa = get_object_or_404(User, id=self.kwargs['pk'])
        return Chamados.objects.filter(idPessoa_id=self.idPessoa)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['idPessoa'] = self.idPessoa
        return context


class FiltrarChamados(ListView):
    template_name = "chamado/chamados_list.html"
    context_object_name = 'chamados_list'

    def get_queryset(self):
        self.idPessoa = get_object_or_404(User, id=self.kwargs['pk'])
        self.idStatus = get_object_or_404(
            Status, id=self.kwargs['statusChamado'])
        return Chamados.objects.filter(idPessoa_id=self.idPessoa, idStatus_id=self.idStatus)


class EditarChamados(UpdateView):
    model = Chamados
    form_class = ChamadosForm
    template_name = "chamado/chamados_edit.html"
    success_url = reverse_lazy('testeHome')


class AbrirChamado(CreateView):
    model = Chamados
    form_class = ChamadosForm
    template_name = "chamado/chamados_abrir.html"
    success_url = reverse_lazy('testeHome')


def home_ajax_search(request, search_string=None):
    if search_string is None:
        servicos_list = Eventos.objects.all()
    else:
        servicos_list = Eventos.objects.filter(
            descricao__icontains=search_string)
        paginator = Paginator(servicos_list, 9)
        page = request.GET.get('page')
        servicos_list = paginator.get_page(page)
    return render(request, 'chamado/servicoSearch.html', {'servicos_list': servicos_list})


def chamados(request,idEvento=None,idChamado='selecionar'):
    meusEnderecos = Endereco.objects.filter(idPessoa_id=request.user.id)
    evento = get_object_or_404(Eventos, pk=idEvento)
    if request.method == 'POST':
        formChamado = ChamadosForm(request.POST)
        if formChamado.is_valid():
            formChamado.save()
            return redirect('chamado:listar_chamados')
        else:
            return HttpResponse(formChamado.errors)
    else:
        formChamado = ChamadosForm()
        context = {'formChamado': formChamado, 'meusEnderecos': meusEnderecos, 'evento': evento}
        return render(request, 'chamado/addChamado.html', context)
        #return HttpResponse(evento.id)
