from django.db import models

# Create your models here.
class Funcionario(models.Model):
    Nome = models.CharField(max_length=100,help_text="Nome do funcionário")