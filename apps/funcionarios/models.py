from datetime import datetime

from django.db import models
from django.templatetags.tz import utc
from  django.urls import reverse
from django.contrib.auth.models import User
from apps.departamento.models import Departamento
from apps.empresas.models import Empresa



class Funcionario(models.Model):
    nome = models.CharField(max_length=100,help_text="Nome do funcionário",null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    data_contratacao = models.DateTimeField(default=datetime(2023,1,1))
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa,on_delete=models.SET_NULL,null=True)

    def get_absolute_url(self):
        return reverse('list_funcionarios')

    def __str__(self):
        return self.nome

