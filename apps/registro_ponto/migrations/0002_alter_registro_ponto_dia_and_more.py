# Generated by Django 4.2.4 on 2023-08-20 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_ponto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_ponto',
            name='dia',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro_ponto',
            name='hora_entrada_lunch',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro_ponto',
            name='hora_fim',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro_ponto',
            name='hora_fim_extra',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro_ponto',
            name='hora_ini',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro_ponto',
            name='hora_ini_extra',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='registro_ponto',
            name='hora_retorno_lunch',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
