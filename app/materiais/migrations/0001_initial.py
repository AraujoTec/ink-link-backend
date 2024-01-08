# Generated by Django 5.0 on 2023-12-29 12:51

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Materiais',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100)),
                ('custo', models.IntegerField()),
                ('preco_revenda', models.IntegerField()),
                ('data_validade', models.DateField(default=None)),
                ('data_criacao', models.DateField(default=None)),
                ('estoque', models.IntegerField()),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresas')),
            ],
            options={
                'verbose_name': 'material',
                'verbose_name_plural': 'materiais',
                'db_table': 'materiais',
            },
        ),
    ]
