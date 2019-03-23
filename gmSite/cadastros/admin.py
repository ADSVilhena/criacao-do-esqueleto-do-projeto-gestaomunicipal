from django.contrib import admin

from .models import Pessoa
from .models import Orgao
from .models import Bairro
from .models import Endereco
from .models import TipoTelefone
from .models import Telefone



admin.site.register(Pessoa)
admin.site.register(Orgao)
admin.site.register(Bairro)
admin.site.register(Endereco)
admin.site.register(TipoTelefone)
admin.site.register(Telefone)