# Generated by Django 5.0 on 2024-01-18 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('materiais', '0002_rename_empresa_materiais_empresa_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='materiais',
            old_name='empresa_id',
            new_name='empresa',
        ),
    ]