from django.contrib import admin

from .models import Pessoa
from .models import Orgao
from .models import Bairro
from .models import Endereco
from .models import TipoTelefone
from .models import Telefone
from .models import Eventos
from .models import Status
from .models import TipoLotacao
from .models import Lotacao
from .models import Chamado


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
admin.site.register(Lotacao,LotacaoAdmin)
