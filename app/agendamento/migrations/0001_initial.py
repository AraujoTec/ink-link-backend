# Generated by Django 5.0 on 2023-12-26 21:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_agendamento', models.DateField(blank=True, null=None)),
                ('data_pagamento', models.DateField(blank=True, null=None)),
                ('taxa_maquina', models.CharField(blank=True, default='', max_length=100, null=None)),
            ],
            options={
                'verbose_name': 'Agendamento',
                'verbose_name_plural': 'Agendamentos',
                'db_table': 'agendamento',
            },
        ),
    ]