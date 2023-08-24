# Generated by Django 4.2.4 on 2023-08-20 14:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('funcionarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Ponto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(auto_now=True)),
                ('hora_ini', models.DateField(auto_now=True)),
                ('hora_entrada_lunch', models.DateField(auto_now=True)),
                ('hora_retorno_lunch', models.DateField(auto_now=True)),
                ('hora_fim', models.DateField(auto_now=True)),
                ('hora_ini_extra', models.DateField(auto_now=True)),
                ('hora_fim_extra', models.DateField(auto_now=True)),
                ('funcionario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='funcionarios.funcionario')),
            ],
        ),
    ]
