# Generated by Django 5.0 on 2023-12-21 14:42

import django.db.models.deletion
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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('custo', models.IntegerField()),
                ('preco_revenda', models.IntegerField()),
                ('data_validade', models.DateField(default=None)),
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
