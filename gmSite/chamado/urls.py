from django.urls import path

from . import views


app_name = 'chamados'
urlpatterns = [
    path('<int:pk>', views.ListarChamados.as_view(), name='listar_chamados'),
    path('<int:pk>/<int:statusChamado>', views.FiltrarChamados.as_view(), name='filtrar_chamados'),
    path('editar/<int:pk>', views.EditarChamados.as_view(), name='editar_chamado'),
    path('abrir/<int:pk>', views.AbrirChamado.as_view(), name='abrir_chamado'),
]
