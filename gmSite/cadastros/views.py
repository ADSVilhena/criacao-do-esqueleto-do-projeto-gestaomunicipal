from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import NameForm

# View de Cadastros


def index(request):
    return HttpResponse("Cadastros")


def cadastrar(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:

            return HttpResponse("clicado com sucesso....mas nada foi salvo hehehe")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'cadastros/cadastro.html', {'form': form})