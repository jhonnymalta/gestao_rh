from django.db import models
from django.urls import reverse

class Departamento(models.Model):
    nome = models.CharField(max_length=50,help_text="Nome do Departamento")

    def get_absolute_url(self):
        return reverse('list_departamento')
    def __str__(self):
        return self.nome