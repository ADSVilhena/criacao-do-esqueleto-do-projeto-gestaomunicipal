from django.contrib import admin
from .models import Pessoa
from .models import Orgao
from .models import Eventos
from .models import Lotacao
from .models import TipoLotacao
from .models import Status

# Register your models here.

class OrgaoAdmin(admin.ModelAdmin):
    list_display = ('nome','cnpj','descricao')
    list_filter = ['nome','cnpj','descricao']

class EventosAdmin(admin.ModelAdmin):
    list_display = ('descricao','idOrgão')
    list_filter = ['descricao']

admin.site.register(Orgao, OrgaoAdmin)
admin.site.register(Eventos)
admin.site.register(Status)
admin.site.register(TipoLotacao)
admin.site.register(Lotacao)



