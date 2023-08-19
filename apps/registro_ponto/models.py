from datetime import datetime

from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Registro_Ponto(models.Model):
    dia = models.DateTimeField(default=datetime.now())
    hora_ini = models.DateTimeField(default=datetime.now())
    hora_entrada_lunch = models.DateTimeField(default=datetime.now())
    hora_retorno_lunch = models.DateTimeField(default=datetime.now())
    hora_fim = models.DateTimeField(default=datetime.now())
    hora_ini_extra = models.DateTimeField(default=datetime.now())
    hora_fim_extra = models.DateTimeField(default=datetime.now())
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)

