# Generated by Django 5.0.6 on 2024-07-04 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contatoformulario',
            name='telefone',
            field=models.CharField(max_length=14, verbose_name='Telefone'),
        ),
    ]