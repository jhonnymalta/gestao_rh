from django.db import models
from apps.funcionarios.models import Funcionario

# Create your models here.
class Registro_Ponto(models.Model):
    dia = models.DateTimeField()
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)

