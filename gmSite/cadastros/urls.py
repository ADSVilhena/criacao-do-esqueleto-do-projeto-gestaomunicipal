from django.urls import path

from . import views


app_name = 'cadastros'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.CriarCadastro.as_view(), name='cadastrar'),
    path('edit/<int:pk>', views.AtualizarCadastro.as_view(), name='atualizar'),
    path('address/<int:idRua>', views.manterEndereco, name='endereco'),
    path('rua/<int:idRua>/<str:idEndereco>', views.ruaSelecionada, name='ruaSelecionada'),
    path('address/listar/<int:pk>',
         views.ListarEnderecos.as_view(), name='listar_enderecos'),
    path('address/listar/',
         views.enderecosList, name='enderecosList'),
    path('address/edit/<int:pk>', views.AtualizarEndereco.as_view(),
         name='endereco_atualizar'),
    path('address/delete/<int:pk>', views.DeletarEndereco.as_view(),
         name='endereco_deletar'),
    path('phone/', views.meusTelefones, name='telefone'),
    path('phone/edit/<int:idTelefone>', views.meusTelefones,
         name='telefone_atualizar'),
    path('phone/delete/<int:pk>', views.DeletarTelefone.as_view(),
         name='telefone_deletar'),
    path('phone/listar/<int:userID>',
         views.ListarTelefones.as_view(), name='listar_telefones'),
    path('phone/listar/',
         views.telefonesList, name='telefonesList'),
    path('success', views.sucesso, name='sucesso'),
    path('ajax-search/<str:search_string>', views.home_ajax_search, name='pesquisa'),
    path('ajax-search/', views.home_ajax_search, name='pesquisa'),
]
