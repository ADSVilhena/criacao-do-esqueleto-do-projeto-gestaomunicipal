from django.urls import path

from . import views


app_name = 'cadastros'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.CriarCadastro.as_view(), name='cadastrar'),
    path('edit/<int:pk>', views.AtualizarCadastro.as_view(), name='atualizar'),
    path('address/', views.manterEndereco, name='endereco'),
    path('address/listar/<int:pk>',
         views.ListarEnderecos.as_view(), name='listar_enderecos'),
    path('address/listar/',
         views.enderecosList, name='enderecosList'),
    path('address/edit/<int:pk>', views.AtualizarEndereco.as_view(),
         name='endereco_atualizar'),
    path('address/delete/<int:pk>', views.DeletarEndereco.as_view(),
         name='endereco_deletar'),
    path('phone/', views.manterTelefone, name='telefone'),
    path('phone/edit/<int:pk>', views.AtualizarTelefone.as_view(),
         name='telefone_atualizar'),
    path('phone/delete/<int:pk>', views.DeletarTelefone.as_view(),
         name='telefone_deletar'),
    path('phone/listar/<int:userID>',
         views.ListarTelefones.as_view(), name='listar_telefones'),
    path('phone/listar/',
         views.telefonesList, name='telefonesList'),
    path('success', views.sucesso, name='sucesso'),
]
