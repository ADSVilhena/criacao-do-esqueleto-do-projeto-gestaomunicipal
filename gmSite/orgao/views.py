from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Lotacao, Orgao, Eventos
from chamado.models import Chamados
# Create your views here.
def retornaLotacao(request):
    lotacao = Lotacao.objects.filter(idPessoa=request.user.id)
    return HttpResponse(lotacao)


def chamadosOrgao(request, pkOrgao=None, pkStatus=None):
    if pkStatus is not None:
        chamado = Chamados.objects.filter(idStatus=pkStatus,idEvento__idOrgao=pkOrgao)
        return HttpResponse(chamado)

    else:
        return HttpResponse("vixi")