from django.contrib import admin
from .models import Pessoa
from .models import Orgao
from .models import Eventos

# Register your models here.

class OrgaoAdmin(admin.ModelAdmin):
    list_display = ('nome','cnpj','descricao')
    list_filter = ['nome','cnpj','descricao']

class EventosAdmin(admin.ModelAdmin):
    list_display = ('descricao','idOrgão')
    list_filter = ['descricao']

admin.site.register(Orgao, OrgaoAdmin)
