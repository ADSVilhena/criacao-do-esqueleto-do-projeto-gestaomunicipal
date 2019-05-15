from django.contrib import admin
from django.contrib.auth.models import User
#from .models import Pessoa
from .models import Endereco
from .models import Eventos
from .models import Status
from .models import Chamados
from orgao.models import Orgao


# Register your models here.

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('idPessoa', 'idEvento', 'idEndereco', 'idStatus', 'dataAbertura', 'dataFechamento', 'observacao')
    list_filter = ['idStatus','idEndereco', 'idEvento', 'dataAbertura', 'dataFechamento','idEvento__idOrgao__nome']


class StatusAdmin(admin.ModelAdmin):
    list_display = ('descricao',)
    list_filter = ['descricao']

admin.site.register(Chamados,ChamadoAdmin)
admin.site.register(Status,StatusAdmin)
