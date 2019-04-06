from django.contrib import admin

from .models import Pessoa
from .models import Bairro
from .models import Endereco
from .models import TipoTelefone
from .models import Telefone


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','cpf','email', 'senha',)
    list_filter = []

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('idPessoa', 'nome', 'numero', 'complemento', 'idBairro', )
    list_filter = ['idPessoa', 'idBairro']

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('idPessoa', 'idTipoTelefone', 'numero')
    list_filter = ['idPessoa', 'idTipoTelefone']

admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Bairro)
admin.site.register(Endereco,EnderecoAdmin)
admin.site.register(TipoTelefone)
admin.site.register(Telefone,TelefoneAdmin)
