# Generated by Django 5.0.6 on 2024-07-05 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0004_alter_contato_telefone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='facebook',
            field=models.CharField(default='', max_length=150, verbose_name='Facebook'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contato',
            name='instagram',
            field=models.CharField(default='', max_length=150, verbose_name='Instagram'),
            preserve_default=False,
        ),
    ]