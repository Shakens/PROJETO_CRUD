from django.db import models
from django.utils import timezone

# Modelo TipoSensor já existente
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

# Modelo Dashboard já existente
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

# Modelo Parametro já existente
class Parametro(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Parâmetro")
    unidade = models.CharField(max_length=20, verbose_name="Unidade de Medida")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Parâmetro"
        verbose_name_plural = "Parâmetros"

# Novo modelo LeituraTemperatura
class LeituraTemperatura(models.Model):
    sensor = models.ForeignKey(TipoSensor, on_delete=models.CASCADE)  # Relacionamento com TipoSensor
    temperatura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Temperatura")  # Temperatura
    data_leitura = models.DateTimeField(default=timezone.now, verbose_name="Data da Leitura")  # Data e hora da leitura

    def __str__(self):
        return f"Leitura de {self.sensor.nome} em {self.data_leitura}"

    class Meta:
        verbose_name = "Leitura de Temperatura"
        verbose_name_plural = "Leituras de Temperatura"
