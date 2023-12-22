# Generated by Django 5.0 on 2023-12-22 18:35

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresas', '0010_alter_empresas_data_atualizacao_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servicos',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('servico', models.CharField(max_length=200)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.empresas')),
            ],
            options={
                'verbose_name': 'Servico',
                'verbose_name_plural': 'Servicos',
                'db_table': 'servico',
            },
        ),
    ]
