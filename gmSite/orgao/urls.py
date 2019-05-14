from django.urls import path

from . import views


app_name = 'orgao'
urlpatterns = [
    path('getLotacao/', views.retornaLotacao, name='getLotacao'),
    path('chamados/<str:pkOrgao>/<str:pkStatus>/', views.chamadosOrgao, name='chamados'),
]
