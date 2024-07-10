from django.db import models

class Servico(models.Model):
    imagem = models.ImageField(verbose_name="Imagem", upload_to='core/static/img/servico')
    titulo = models.CharField(verbose_name="Título", max_length=100)
    alt = models.CharField(verbose_name="Texto Alternativo", max_length=100)

    class Meta:
        verbose_name = "Serviço"
        db_table = 'servico'

    def __str__(self):
        return self.titulo


class NossosServicos(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    descricao = models.TextField(verbose_name="Descrição")

    class Meta:
        verbose_name = "Nosso Serviço"
        db_table = 'nossos_servicos'

    def __str__(self):
        return self.titulo    
