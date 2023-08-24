from datetime import datetime

from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Registro_Ponto(models.Model):
    dia = models.DateTimeField(default=datetime(2023,1,1))
    hora_ini = models.DateTimeField(default=datetime(2023,1,1))
    hora_entrada_lunch = models.DateTimeField(default=datetime(2023,1,1))
    hora_retorno_lunch = models.DateTimeField(default=datetime(2023,1,1))
    hora_fim = models.DateTimeField(default=datetime(2023,1,1))
    hora_ini_extra = models.DateTimeField(default=datetime(2023,1,1))
    hora_fim_extra = models.DateTimeField(default=datetime(2023,1,1))
    funcionario = models.ForeignKey(Funcionario,on_delete=models.SET_NULL, null=True)

