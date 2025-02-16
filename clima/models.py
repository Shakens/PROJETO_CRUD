from django.db import models
from django.utils import timezone

# Modelo TipoSensor
class TipoSensor(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, null=False)
    limite_inferior_permitido = models.FloatField(null=False)
    limite_superior_permitido = models.FloatField(null=False)
    unidade = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'tb_tiposensor'  # Define o nome exato da tabela

    def __str__(self):
        return f"{self.descricao} ({self.unidade})"


# Modelo Sala
class Sala(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=150, null=False)
    sigla = models.CharField(max_length=10, unique=True, null=False)
    id_pavimento = models.ForeignKey('Pavimento', on_delete=models.RESTRICT, null=True, db_column='id_pavimento')
    id_orientacao = models.ForeignKey('Orientacao', on_delete=models.RESTRICT, null=True, db_column='id_orientacao')

    class Meta:
        db_table = 'tb_sala'  # Nome exato da tabela

    def __str__(self):
        return f"{self.sigla} - {self.nome}"


# Modelo Parametro
class Parametro(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_logico = models.ForeignKey('SensorLogico', on_delete=models.RESTRICT)
    nome = models.CharField(max_length=50)
    valor = models.FloatField()

    class Meta:
        db_table = 'tb_parametro'  # Define o nome exato da tabela

    def __str__(self):
        return f"{self.nome}: {self.valor}"


# Modelo Pavimento
class Pavimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tb_pavimento'  # Define o nome exato da tabela

    def __str__(self):
        return self.nome


# Modelo SensorFisico
class SensorFisico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    sigla = models.CharField(max_length=10, unique=True, null=False)
    descricao = models.CharField(max_length=150, null=True, blank=True)
    tensao_min = models.FloatField(null=False)
    tensao_max = models.FloatField(null=False)

    class Meta:
        db_table = 'tb_sensorfisico'  # Define o nome exato da tabela

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


# Modelo SensorLogico
class SensorLogico(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_fisico = models.ForeignKey(SensorFisico, on_delete=models.RESTRICT, related_name="sensor_logicos")
    tipo = models.ForeignKey(TipoSensor, on_delete=models.RESTRICT, related_name="sensor_logicos")
    descricao = models.CharField(max_length=50, null=False)

    class Meta:
        db_table = 'tb_sensorlogico'

    def __str__(self):
        return f"{self.descricao} ({self.sensor_fisico.nome})"




# Modelo Orientacao
class Orientacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'tb_orientacao'  # Define o nome exato da tabela

    def __str__(self):
        return self.nome


# Modelo Relatorio
class Relatorio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Relatório")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    class Meta:
        db_table = 'tb_relatorio'  # Define o nome exato da tabela
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"

    def __str__(self):
        return self.nome


# Modelo LeituraSensor
class LeituraSensor(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_logico = models.ForeignKey(SensorLogico, on_delete=models.RESTRICT, related_name="leituras_sensores")
    leitura = models.ForeignKey('Leitura', on_delete=models.CASCADE, related_name="leituras_sensores")
    valor = models.FloatField()

    class Meta:
        db_table = 'tb_leitura_sensor'  # Define o nome exato da tabela

    def __str__(self):
        return f"Leitura {self.leitura.id} - Sensor {self.sensor_logico.nome}: {self.valor}"


# Modelo Leitura
class Leitura(models.Model):
    id = models.AutoField(primary_key=True)
    sala = models.ForeignKey(Sala, on_delete=models.RESTRICT, related_name="leituras")
    data_hora = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'tb_leitura'  # Define o nome exato da tabela

    def __str__(self):
        return f"Leitura {self.id} - Sala {self.sala.nome} em {self.data_hora}"
