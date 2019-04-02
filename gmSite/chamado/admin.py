from django.contrib import admin
from .models import Pessoa
from .models import Endereco
from .models import Eventos
from .models import Status
from .models import Chamados


# Register your models here.

class ChamadoAdmin(admin.ModelAdmin):
    list_display = ('idPessoa', 'idEvento', 'idEndereco', 'idStatus', 'dataAbertura', 'dataFechamento', 'observacao')
    list_filter = ['idStatus','idEndereco', 'idEvento', 'dataAbertura', 'dataFechamento']


admin.site.register(Chamados,ChamadoAdmin)