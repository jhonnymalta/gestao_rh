from django.db import models
from  apps.funcionarios.models import Funcionario

# Create your models here.
class Documento(models.Model):
    nome = models.CharField(max_length=25)
    pertencente = models.ForeignKey(Funcionario,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.nome
