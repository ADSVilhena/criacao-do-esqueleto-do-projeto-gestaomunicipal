from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Lotacao, Orgao, Eventos
from chamado.models import Chamados
# Create your views here.
def retornaLotacao(request):
    lotacao = Lotacao.objects.filter(idPessoa=request.user.id)
    context = {'userServidor': lotacao}
    return render(request, 'gmSite/index.html', context)


def chamadosOrgao(request, pkOrgao=None, pkStatus=None):
    if pkStatus is not None:
        chamado = Chamados.objects.filter(idStatus=pkStatus,idEvento__idOrgao=pkOrgao)
        context = {'chamados_list': chamado}
        return render(request, 'orgao/chamadosOrgao.html', context)

    else:
        return HttpResponse("vixi")