# Generated by Django 5.0 on 2023-12-29 12:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authenticate', '0001_initial'),
        ('cargos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('deleted', models.BooleanField(default=False)),
                ('data_nascimento', models.DateField(blank=True, default=None, null=True)),
                ('cpf', models.CharField(max_length=11)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cargos.cargos')),
            ],
            options={
                'verbose_name': 'colaborador',
                'verbose_name_plural': 'Colaboradores',
                'db_table': 'colaborador',
            },
            bases=('authenticate.user', models.Model),
        ),
    ]
