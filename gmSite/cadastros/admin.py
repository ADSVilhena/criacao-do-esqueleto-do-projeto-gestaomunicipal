from django.contrib import admin
from django.contrib.auth.models import User

#from .models import Pessoa
from .models import Bairro
from .models import Endereco
from .models import TipoTelefone
from .models import Telefone
from .models import Rua



class PessoaAdmin(admin.ModelAdmin):
    list_display = ('id','nome','cpf','email', 'senha',)
    list_filter = []

class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('idPessoa', 'idRua', 'numero', 'complemento', )
    list_filter = ['idPessoa',]

class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('idPessoa', 'idTipoTelefone', 'numero')
    list_filter = ['idPessoa', 'idTipoTelefone']

class RuaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'idBairro')    

class PessoaUserAdmin(admin.ModelAdmin):
    list_display = ('first_name',)
    list_filter = []    

#admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Bairro)
admin.site.register(Endereco,EnderecoAdmin)
admin.site.register(TipoTelefone)
admin.site.register(Telefone,TelefoneAdmin)
admin.site.register(Rua,RuaAdmin)
