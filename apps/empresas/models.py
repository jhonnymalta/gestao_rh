from django.db import models


class Empresa(models.Model):
    Nome = models.CharField(max_length=100,help_text="Nome da empresa")

    def __str__(self):
        return self.Nome