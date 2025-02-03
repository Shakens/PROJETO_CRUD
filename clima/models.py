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

# Novo modelo Pavimento
class Pavimento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Pavimento")
    descricao = models.TextField(verbose_name="Descrição")
    andar = models.PositiveIntegerField(verbose_name="Número do Andar")  # Andar do pavimento
    localizacao = models.CharField(max_length=100, verbose_name="Localização")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Pavimento"
        verbose_name_plural = "Pavimentos"

# Novo modelo SensorFisico
class SensorFisico(models.Model):
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.CASCADE, verbose_name="Tipo de Sensor")
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, verbose_name="Sala")
    pavimento = models.ForeignKey(Pavimento, on_delete=models.CASCADE, verbose_name="Pavimento")
    localizacao = models.CharField(max_length=100, verbose_name="Localização")
    data_instalacao = models.DateField(default=timezone.now, verbose_name="Data de Instalação")
    ativo = models.BooleanField(default=True, verbose_name="Sensor Ativo")

    def __str__(self):
        return f"Sensor {self.tipo_sensor.nome} instalado em {self.sala.nome} - {self.pavimento.nome}"

    class Meta:
        verbose_name = "Sensor Físico"
        verbose_name_plural = "Sensores Físicos"

# Novo modelo SensorLogico
class SensorLogico(models.Model):
    tipo_sensor = models.ForeignKey(TipoSensor, on_delete=models.CASCADE, verbose_name="Tipo de Sensor")
    sensor_fisico = models.ForeignKey(SensorFisico, on_delete=models.CASCADE, verbose_name="Sensor Físico", related_name="logico")
    descricao = models.CharField(max_length=255, verbose_name="Descrição")
    ativo = models.BooleanField(default=True, verbose_name="Sensor Ativo")
    data_instalacao = models.DateField(default=timezone.now, verbose_name="Data de Instalação")

    def __str__(self):
        return f"Sensor Lógico {self.tipo_sensor.nome} relacionado ao {self.sensor_fisico}"

    class Meta:
        verbose_name = "Sensor Lógico"
        verbose_name_plural = "Sensores Lógicos"

# Novo modelo Orientacao
class Orientacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da Orientação")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Orientação"
        verbose_name_plural = "Orientações"

# Novo modelo Relatorio
class Relatorio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Relatório")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatorios"
