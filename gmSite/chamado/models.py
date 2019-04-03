from django.db import models
from cadastros.models import Pessoa
from cadastros.models import Endereco
from orgao.models import Eventos
from orgao.models import Status


# Create your models here.

class Chamados(models.Model):
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE,verbose_name="PESSOA")
    idEvento = models.ForeignKey(Eventos, on_delete=models.CASCADE,verbose_name="SERVIÇO")
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE,verbose_name="ENDEREÇO")
    idStatus = models.ForeignKey(Status, on_delete=models.CASCADE,verbose_name="STATUS")
    dataAbertura = models.DateField('ABERTO EM',default=None)
    dataFechamento = models.DateField('CONCLUÍDO EM',default=None, blank=True, null=True)
    observacao = models.CharField('OBSERVAÇÃO',max_length=200)

    def __str__(self):
        return self.idPessoa.nome + " - " + self.idEvento.descricao + " - " + self.idEndereco.nome + " - " + self.idEndereco.numero

    class Meta:
        verbose_name = "Chamado"
        verbose_name_plural = "Chamados"