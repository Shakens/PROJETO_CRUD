from django.db import models

class TipoSensor(models.Model):
    nome = models.CharField(max_length=100)
    sigla = models.CharField(max_length=10)
    descricao = models.TextField()
    limite_inferior_permitido = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome
