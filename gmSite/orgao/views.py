from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from .models import Lotacao, Orgao, Eventos
from chamado.models import Chamados
# Create your views here.

def index(request):
    idOrgao = request.GET.get('idOrgao')
    context = {'orgaoSelecionado': idOrgao}
    return render(request, 'orgao/index.html', context)

def gerenciarChamados(request):
    return render(request, 'orgao/gerenciaChamados.html')

def retornaLotacao(request):    
    lotacao = Lotacao.objects.filter(idPessoa=request.user.id)
    context = {'userServidor': lotacao}
    if request.method == 'POST':
        idOrgaoVinculo = request.POST.get('idOrgao')
        orgaoVinculo = get_object_or_404(Orgao, pk=idOrgaoVinculo)
        request.session['idVinculo'] = idOrgaoVinculo
        request.session['nomeVinculo'] = orgaoVinculo.nome
        return redirect('testeHome')
    else:
        if len(lotacao) == 0:
            return render(request, 'gmSite/index.html', context)
        else:
            return render(request, 'orgao/escolheVinculo.html', context)
    return HttpResponse(request.POST.get('idOrgao'))


def chamadosOrgao(request, pkOrgao=None, pkStatus=None):
    if pkStatus is not None:
        chamado = Chamados.objects.filter(idStatus=pkStatus,idEvento__idOrgao=pkOrgao)
        context = {'chamados_list': chamado}
        return render(request, 'orgao/chamadosOrgao.html', context)

    else:
        return HttpResponse("vixi")