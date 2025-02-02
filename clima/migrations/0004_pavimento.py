# Generated by Django 5.1.5 on 2025-02-02 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0003_leituratemperatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pavimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Pavimento')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('andar', models.PositiveIntegerField(verbose_name='Número do Andar')),
                ('localizacao', models.CharField(max_length=100, verbose_name='Localização')),
            ],
            options={
                'verbose_name': 'Pavimento',
                'verbose_name_plural': 'Pavimentos',
            },
        ),
    ]
