from django.db import models

class TipoSensor(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Sensor")
    sigla = models.CharField(max_length=10, verbose_name="Sigla")
    descricao = models.TextField(verbose_name="Descrição")
    limite_inferior_permitido = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Limite Inferior Permitido"
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Sensor"
        verbose_name_plural = "Tipos de Sensores"


class Dashboard(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Dashboard")
    descricao = models.TextField(verbose_name="Descrição")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Dashboard"
        verbose_name_plural = "Dashboards"


# Alterado de Sala para Salas
class Sala(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Sala")
    descricao = models.TextField(verbose_name="Descrição")
    capacidade = models.PositiveIntegerField(verbose_name="Capacidade da Sala")  # Usando PositiveIntegerField
    localizacao = models.CharField(max_length=100, verbose_name="Localização")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Sala"
        verbose_name_plural = "Salas"
