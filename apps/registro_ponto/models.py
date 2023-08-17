from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Registro_Ponto(models.Model):
    dia = models.DateTimeField()
    hora_ini = models.DateTimeField()
    hora_entrada_lunch = models.DateTimeField()
    hora_retorno_lunch = models.DateTimeField()
    hora_fim = models.DateTimeField()
    hora_ini_extra = models.DateTimeField()
    hora_fim_extra = models.DateTimeField()
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)

