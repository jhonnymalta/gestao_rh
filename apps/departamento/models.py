from django.db import models

# Create your models here.
class Departamento(models.Model):
    Nome = models.CharField(max_length=50,help_text="Nome do Departamento")


    def __str__(self):
        return self.Nome