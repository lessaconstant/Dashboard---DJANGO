from django.db import models

class Dados(models.Model):
    inscricao = models.CharField(max_length=20, unique=True)
    faixa_idade = models.CharField(max_length=2)
    sexo = models.CharField(max_length=1)
    estado_civil = models.CharField(max_length=1)
    raca = models.CharField(max_length=1)
    nacionalidade = models.CharField(max_length=1)
    conclusao_status = models.CharField(max_length=1)
    conclusao_ano = models.CharField(max_length=2)
    tipo_escola = models.CharField(max_length=1)
    conclusao_situacao = models.CharField(max_length=1)
    treineiro = models.BooleanField()
    CN = models.DecimalField(max_digits=5, decimal_places=2)
    CH = models.DecimalField(max_digits=5, decimal_places=2)
    LC = models.DecimalField(max_digits=5, decimal_places=2)
    MT = models.DecimalField(max_digits=5, decimal_places=2)
    REDACAO = models.DecimalField(max_digits=5, decimal_places=2)
    MEDIA = models.DecimalField(max_digits=5, decimal_places=2)
# Create your models here.
