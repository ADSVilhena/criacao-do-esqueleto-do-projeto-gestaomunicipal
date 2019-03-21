from django.db import models

#Models de Bairros

class Bairro(model.Model):
    nome_bairro = models.CharField(max_length=30)
