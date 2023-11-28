# Generated by Django 4.2.7 on 2023-11-28 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=200)),
                ('nome_fantasia', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=14)),
                ('telefone', models.CharField(max_length=11)),
                ('user_criacao', models.CharField(max_length=200)),
                ('user_alteracao', models.CharField(max_length=200)),
                ('data_cadastro', models.DateTimeField(default=datetime.datetime(2023, 11, 28, 17, 41, 54, 554402))),
                ('data_atualizacao', models.DateTimeField(default=None)),
                ('excluido', models.BooleanField(default=False)),
            ],
        ),
    ]