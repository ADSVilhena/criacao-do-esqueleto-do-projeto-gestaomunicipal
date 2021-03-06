from django.urls import path

from . import views


app_name = 'orgao'
urlpatterns = [
    path('', views.index, name="index"),
    path('getLotacao/', views.retornaLotacao, name='getLotacao'),
    path('chamados/<str:pkOrgao>/<str:pkStatus>/', views.chamadosOrgao, name='chamados'),
    path('chamados/<str:pkOrgao>/', views.chamadosOrgao, name='chamados'),
    path('gerenciar/chamado/<str:pkChamado>/', views.gerenciarChamados, name='gerenciarChamados'),
]
