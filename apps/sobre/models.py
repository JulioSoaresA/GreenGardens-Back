from django.db import models


class Intro(models.Model):
    imagem = models.ImageField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/intro')
    titulo = models.CharField(verbose_name='Título', max_length=100)
    alt = models.CharField(verbose_name='Texto Alternativo', max_length=100)

    class Meta:
        verbose_name = 'Introdução'
        verbose_name_plural = 'Introdução'
        db_table = 'intro'

    def __str__(self):
        return self.titulo


class NossosValores(models.Model):
    titulo = models.CharField(verbose_name='Título', max_length=100)
    descricao = models.TextField(verbose_name='Descrição')

    class Meta:
        verbose_name = 'Nosso Valor'
        verbose_name_plural = 'Nossos Valores'
        db_table = 'nossos_valores'


class Valores(models.Model):
    imagem = models.ImageField('Foto de Exibição', null=True, blank=True, upload_to='core/static/img/valores')
    titulo = models.CharField(verbose_name='Título', max_length=100)
    descricao = models.TextField(verbose_name='Descrição')
    alt = models.CharField(verbose_name='Texto Alternativo', max_length=100)

    class Meta:
        verbose_name = 'Valor'
        verbose_name_plural = 'Valores'
        db_table = 'valores'

    def __str__(self):
        return self.titulo
