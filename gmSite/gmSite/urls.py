from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('cadastros/', include('cadastros.urls')),
    path('chamados/', include('chamado.urls')),
    path('orgao/', include('orgao.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('', TemplateView.as_view(template_name='gmSite/index.html'), name="testeHome"),
    #path('index/', TemplateView.as_view(template_name='testeHome.html'), name="testeHome"),
]