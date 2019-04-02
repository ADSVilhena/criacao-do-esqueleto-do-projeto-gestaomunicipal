from django.contrib import admin

from .models import Pessoa
from .models import Orgao 
from .models import Bairro
from .models import Endereco
from .models import TipoTelefone
from .models import Telefone
from orgao.models import Eventos
from orgao.models import Status
from orgao.models import TipoLotacao
from orgao.models import Lotacaos


class LotacaoAdmin(admin.ModelAdmin):
    list_display = ('idOrgao','idPessoa','idTipoLotacao','observacao')
    list_filter = ['idOrgao']




admin.site.register(Pessoa)
admin.site.register(Orgao)
admin.site.register(Bairro)
admin.site.register(Endereco)
admin.site.register(TipoTelefone)
admin.site.register(Telefone)
admin.site.register(Eventos)
admin.site.register(Status)
admin.site.register(TipoLotacao)
admin.site.register(Lotacaos,LotacaoAdmin)
