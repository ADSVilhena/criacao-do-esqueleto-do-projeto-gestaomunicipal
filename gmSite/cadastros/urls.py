from django.urls import path

from . import views


app_name = 'cadastros'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.CriarCadastro.as_view(), name='cadastrar'),
    path('edit/<int:pk>', views.AtualizarCadastro.as_view(), name='atualizar'),
    path('address/', views.CriarEndereco.as_view(), name='endereco'),
    path('address/listar', views.ListarEnderecos.as_view(), name='listar_enderecos'),
    path('address/edit/<int:pk>', views.AtualizarEndereco.as_view(), name='endereco_atualizar'),
    path('phone/', views.CriarTelefone.as_view(), name='telefone'),
    path('phone/edit/<int:pk>', views.AtualizarTelefone.as_view(), name='telefone_atualizar'),          
    path('success', views.sucesso, name='sucesso'),
]
