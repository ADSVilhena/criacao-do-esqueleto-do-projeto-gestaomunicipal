from django.db import models

# Models de cadastro

class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11)
    senha = models.CharField(max_length=11)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Orgao(models.Model):
    nome = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=14)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
 

class Bairro(models.Model):
    nome = models.CharField(max_length=30)

    def __str__(self):
        return self.nome


class Endereco(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=50)
    idBairro = models.ForeignKey(Bairro, on_delete=models.CASCADE)
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class TipoTelefone(models.Model):
    descricao = models.CharField(max_length=20)

    def __str__(self):
        return self.descricao


class Telefone(models.Model):
    numero = models.CharField(max_length=11)
    idTipoTelefone = models.ForeignKey(TipoTelefone, on_delete=models.CASCADE)
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)


    def __str__(self):
        return self.numero


class Eventos(models.Model):
    descricao = models.CharField(max_length=50)
    idOrgao = models.ForeignKey(Orgao, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao


class Status(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class TipoLotacao(models.Model):
    descricao = models.CharField(max_length=50)

    def __str__(self):
        return self.descricao


class Lotacao(models.Model):
    idTipoLotacao = models.ForeignKey(TipoLotacao, on_delete=models.CASCADE)
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    idOrgao = models.ForeignKey(Orgao, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.idTipoLotacao


class Chamado(models.Model):
    idPessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    idEvento = models.ForeignKey(Eventos, on_delete=models.CASCADE)
    idEndereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    idStatus = models.ForeignKey(Status, on_delete=models.CASCADE)
    dataAbertura = models.CharField(max_length=10)
    dataFechamento = models.CharField(max_length=10)
    observacao = models.CharField(max_length=200)

    def __str__(self):
        return self.observacao