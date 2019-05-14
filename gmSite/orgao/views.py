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
        servicosOrgao = Eventos.objects.filter(idOrgao=pkOrgao)
        context = {}
        contador = 0
        for s in servicosOrgao:
            dados = Chamados.objects.filter(idEvento=s,idStatus=pkStatus)
            contador = contador + 1
            context[contador] = dados
        return HttpResponse(context)

    else:
        return HttpResponse("vixi")