from django.contrib import admin
from django.contrib.auth.models import User
#from .models import Pessoa
from .models import Orgao
from .models import Eventos
from .models import Lotacao
from .models import TipoLotacao


# Register your models here.

class OrgaoAdmin(admin.ModelAdmin):
    list_display = ('nome','cnpj','descricao')
    list_filter = ['nome','cnpj','descricao']

class EventosAdmin(admin.ModelAdmin):
    list_display = ('descricao','idOrgao')
    list_filter = ['descricao','idOrgao']

class LotacaoAdmin(admin.ModelAdmin):
    list_display = ('idOrgao','idPessoa','idTipoLotacao','observacao')
    list_filter = ['idOrgao']

class TipoLotacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ['descricao',]

admin.site.register(Orgao, OrgaoAdmin)
admin.site.register(Eventos,EventosAdmin)
admin.site.register(TipoLotacao,TipoLotacaoAdmin)
admin.site.register(Lotacao,LotacaoAdmin)



