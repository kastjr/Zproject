from django.db import models
from datetime import datetime
from django.utils.safestring import mark_safe

class Sobrevivente(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=2)
    localizacao = models.CharField(max_length=100)
    denuncias = models.IntegerField(default=0)
    agua = models.IntegerField(default=0)
    medicamento = models.IntegerField(default=0)
    comida = models.IntegerField(default=0)
    municao = models.IntegerField(default=0)
    pontos = models.IntegerField(default=0)
    infectado = models.BooleanField(default=False)


    def __str__(self):
        return self.nome
