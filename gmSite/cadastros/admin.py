from django.contrib import admin

from .models import Pessoa
from .models import Bairro
from .models import Endereco
from .models import TipoTelefone
from .models import Telefone


class LotacaoAdmin(admin.ModelAdmin):
    list_display = ('idOrgao','idPessoa','idTipoLotacao','observacao')
    list_filter = ['idOrgao']




admin.site.register(Pessoa)
admin.site.register(Bairro)
admin.site.register(Endereco)
admin.site.register(TipoTelefone)
admin.site.register(Telefone)
