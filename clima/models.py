from django.db import models
from django.utils import timezone

# Modelo TipoSensor
class TipoSensor(models.Model):
    id = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=50, null=False)
    limite_inferior_permitido = models.FloatField(null=False)
    limite_superior_permitido = models.FloatField(null=False)
    unidade = models.CharField(max_length=45, null=False)

    def __str__(self):
        return f"{self.descricao} ({self.unidade})"


# Alterado de Sala para Salas
class Sala(models.Model):
    id = models.AutoField(primary_key=True)  # Campo ID autoincrement
    nome = models.CharField(max_length=150, null=False)  # Nome da sala (Obrigatório)
    sigla = models.CharField(max_length=10, unique=True, null=False)  # Sigla única (Obrigatório)
    
    # Chaves estrangeiras para Pavimento e Orientação
    id_pavimento = models.ForeignKey('Pavimento', on_delete=models.RESTRICT, null=True, db_column='id_pavimento')
    id_orientacao = models.ForeignKey('Orientacao', on_delete=models.RESTRICT, null=True, db_column='id_orientacao')

    class Meta:
        db_table = 'tb_sala'  # Nome exato da tabela no MySQL

    def __str__(self):
        return f"{self.sigla} - {self.nome}"  # Exibe Sigla + Nome no Django Admin


# Modelo Parametro
class Parametro(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_logico = models.ForeignKey(
        'SensorLogico',  # Nome do modelo referenciado (ajuste se necessário)
        on_delete=models.RESTRICT
    )
    nome = models.CharField(max_length=50)
    valor = models.FloatField()

    def __str__(self):
        return f"{self.nome}: {self.valor}"


# Novo modelo Pavimento
class Pavimento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


# Novo modelo SensorFisico
class SensorFisico(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, null=False)
    sigla = models.CharField(max_length=10, unique=True, null=False)
    descricao = models.CharField(max_length=150, null=True, blank=True)
    tensao_min = models.FloatField(null=False)
    tensao_max = models.FloatField(null=False)

    def __str__(self):
        return f"{self.nome} ({self.sigla})"


# Novo modelo SensorLogico
class SensorLogico(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_fisico = models.ForeignKey(SensorFisico, on_delete=models.RESTRICT)
    tipo = models.ForeignKey(TipoSensor, on_delete=models.RESTRICT)
    descricao = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f"{self.descricao} ({self.sensor_fisico.nome})"


# Novo modelo Orientacao
class Orientacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


# Novo modelo Relatorio
class Relatorio(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome do Relatório")
    descricao = models.TextField(verbose_name="Descrição", blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Relatório"
        verbose_name_plural = "Relatórios"


# Leitura Sensor
class LeituraSensor(models.Model):
    id = models.AutoField(primary_key=True)
    sensor_logico = models.ForeignKey(SensorLogico, on_delete=models.RESTRICT, related_name="leituras_sensores")
    leitura = models.ForeignKey('Leitura', on_delete=models.CASCADE, related_name="leituras_sensores")  # Correção aqui
    valor = models.FloatField()

    def __str__(self):
        return f"Leitura {self.leitura.id} - Sensor {self.sensor_logico.nome}: {self.valor}"


# Leitura
class Leitura(models.Model):
    id = models.AutoField(primary_key=True)
    sala = models.ForeignKey(Sala, on_delete=models.RESTRICT, related_name="leituras")
    data_hora = models.DateTimeField(default=timezone.now)  # Correção aqui

    def __str__(self):
        return f"Leitura {self.id} - Sala {self.sala.nome} em {self.data_hora}"
