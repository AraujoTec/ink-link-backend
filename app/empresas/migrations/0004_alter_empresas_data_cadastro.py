# Generated by Django 4.2.7 on 2023-12-04 20:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0003_alter_empresas_options_alter_empresas_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresas',
            name='data_cadastro',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 4, 17, 30, 10, 989806)),
        ),
    ]
