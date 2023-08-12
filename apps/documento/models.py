from django.db import models

# Create your models here.
class Documento(models.Model):
    Nome = models.CharField(max_length=25)

    def __str__(self):
        return self.Nome
