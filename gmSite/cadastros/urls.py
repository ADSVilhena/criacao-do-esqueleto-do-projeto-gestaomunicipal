from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.cadastrarPessoaUser, name='cadastrar'),
    path('address/<str:cpf>', views.cadastrarEndereco, name='endereco'),
    path('phone/<str:cpf>', views.cadastrarTelefone, name='telefone'),
    path('success/<str:cpf>', views.sucesso, name='sucesso'),
    path('user', views.cadastrarPessoaUser, name='usuario'),
]
