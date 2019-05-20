from django.db import models
from cadastros.models import Endereco
from orgao.models import Eventos
from django.contrib.auth.models import User


# Create your models here.
class Status(models.Model):
    descricao = models.CharField('STATUS',max_length=50)
    

    def __str__(self):
        return self.descricao
        
    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Status"


class Chamados(models.Model):
    idPessoa = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="PESSOA")
    idEvento = models.ForeignKey(Eventos, on_delete=models.CASCADE,verbose_name="SERVIÇO")
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE,verbose_name="ENDEREÇO")
    idStatus = models.ForeignKey(Status, on_delete=models.CASCADE,verbose_name="STATUS",default='1')
    dataAbertura = models.DateField('ABERTO EM',auto_now_add=True)
    dataFechamento = models.DateField('CONCLUÍDO EM',auto_now=True)
    observacao = models.CharField('OBSERVAÇÃO',max_length=200)
    observacaoOrgao = models.CharField('RETORNO DO ÓRGÃO', max_length=500, null=True, blank=True)

    def __str__(self):
        return self.idPessoa.first_name + " - " + self.idEvento.descricao + " - " + self.idEndereco.idRua.nome + " - " + self.idEndereco.numero

    class Meta:
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"

