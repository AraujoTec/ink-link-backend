# Generated by Django 5.0 on 2023-12-22 15:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0006_alter_empresas_data_atualizacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='data_atualizacao',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 22, 12, 10, 41, 17265)),
        ),
        migrations.AlterField(
            model_name='empresas',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 22, 12, 10, 41, 17251)),
        ),
    ]
