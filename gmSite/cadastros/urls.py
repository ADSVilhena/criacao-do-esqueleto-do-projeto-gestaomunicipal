from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.cadastrar, name='cadastrar'),
    path('address/<int:pessoa_id>/', views.cadastrarEndereco, name='endereco'),
    path('phone', views.cadastrarTelefone, name='telefone'),
    path('success', views.sucesso, name='sucesso'),
    path('user', views.dadosUsuario, name='usuario'),
]