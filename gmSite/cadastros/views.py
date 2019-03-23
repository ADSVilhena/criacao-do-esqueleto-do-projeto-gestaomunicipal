from django.shortcuts import render
from django.http import HttpResponse

# View de Cadastros


def index(request):
    return HttpResponse("Cadastros")
