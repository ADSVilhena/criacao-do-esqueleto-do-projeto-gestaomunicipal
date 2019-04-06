from django.db import models
from cadastros.models import Pessoa


class Orgao(models.Model):
    nome = models.CharField('ÓRGÃO',max_length=200)
    cnpj = models.CharField('CNPJ',max_length=14)
    descricao = models.CharField('DESCRIÇÃO',max_length=100)

    def __str__(self):
        return self.nome

class Eventos(models.Model):
    descricao = models.CharField('SERVIÇO',max_length=50)
    idOrgao = models.ForeignKey(Orgao, on_delete=models.CASCADE,verbose_name="ÓRGÃO")

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


class TipoLotacao(models.Model):
    descricao = models.CharField('TIPO LOTAÇÃO',max_length=50)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = "TipoLotacao"
        verbose_name_plural = "TipoLotacao"


class Lotacao(models.Model):
    idTipoLotacao = models.ForeignKey(TipoLotacao, on_delete=models.CASCADE,verbose_name="TIPO LOTAÇÃO")
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE, verbose_name="PESSOA")
    idOrgao = models.ForeignKey(Orgao, on_delete=models.CASCADE,verbose_name="ÓRGÃO")
    observacao = models.CharField('OBSERVAÇÃO',max_length=200)
    
    def __str__(self):
        return self.idPessoa.nome + " - " + self.idOrgao.nome

    class Meta:
        verbose_name = "Lotação"
        verbose_name_plural = "Lotação"