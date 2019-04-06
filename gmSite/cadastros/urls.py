from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.cadastrar, name='cadastrar'),
    path('address', views.cadastrarEndereco, name='endereco'),
    path('phone', views.cadastrarTelefone, name='telefone'),
    path('success', views.sucesso, name='sucesso'),
]