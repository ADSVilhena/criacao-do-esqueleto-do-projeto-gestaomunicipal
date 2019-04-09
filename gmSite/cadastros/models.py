from django.db import models
from django.contrib.auth.models import User

# Models de cadastro

class Pessoa(models.Model):
    nome = models.CharField('PESSOA',max_length=150)
    cpf = models.CharField('CPF',max_length=11)
    senha = models.CharField('SENHA',max_length=11)
    email = models.CharField('E-MAIL',max_length=100)

    def __str__(self):
        return self.nome 

class PessoaUser(User):
    #user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name="Usuário")

    def __str__(self):
        return self.first_name


class Bairro(models.Model):
    nome = models.CharField('BAIRRO',max_length=30)

    def __str__(self):
        return self.nome


class Rua(models.Model):
    nome = models.CharField('RUA', max_length=200)
    idBairro = models.ForeignKey(Bairro, on_delete=models.CASCADE,verbose_name="BAIRRO")

    def __str__(self):
        return self.nome   

class Endereco(models.Model):
    idRua = models.ForeignKey(Rua, on_delete=models.CASCADE,verbose_name="RUA")
    numero = models.CharField('NÚMERO',max_length=5)
    complemento = models.CharField('COMPLEMENTO',max_length=50)
    idPessoa = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="PESSOA")

    def __str__(self):
        return  self.nome + ", " + self.numero + " - " + self.idBairro.nome


class TipoTelefone(models.Model):
    descricao = models.CharField('TIPO TELEFONE',max_length=20)

    def __str__(self):
        return self.descricao


class Telefone(models.Model):
    numero = models.CharField('NÚMERO',max_length=11)
    idTipoTelefone = models.ForeignKey(TipoTelefone, on_delete=models.CASCADE,verbose_name="TIPO TELEFONE")
    idPessoa = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="PESSOA")


    def __str__(self):
        return self.idPessoa.nome + " - " + self.numero




def get_first_name(self):
    return self.first_name

User.add_to_class("__str__", get_first_name)