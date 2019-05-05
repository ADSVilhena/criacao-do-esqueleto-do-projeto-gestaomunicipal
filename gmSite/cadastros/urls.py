from django.urls import path

from . import views


app_name = 'cadastros'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.CriarCadastro.as_view(), name='cadastrar'),
    path('edit/<int:pk>', views.AtualizarCadastro.as_view(), name='atualizar'),
    path('address/', views.manterEndereco, name='endereco'),
    #path('address/', views.manterEndereco, name='manterEndereco'),
    path('address/listar/<int:pk>', views.ListarEnderecos.as_view(), name='listar_enderecos'),
    path('address/edit/<int:pk>', views.AtualizarEndereco.as_view(), name='endereco_atualizar'),
    path('phone/', views.CriarTelefone.as_view(), name='telefone'),
    path('phone/edit/<int:pk>', views.AtualizarTelefone.as_view(), name='telefone_atualizar'),  
    path('phone/delete/<int:pk>', views.DeletarTelefone.as_view(), name='telefone_deletar'), 
    path('phone/listar/<int:userID>', views.ListarTelefones.as_view(), name='listar_telefones'),            
    path('success', views.sucesso, name='sucesso'),
]
