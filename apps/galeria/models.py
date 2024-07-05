from django.db import models

class Galeria(models.Model):
    imagem = models.ImageField(verbose_name="Imagem", upload_to='core/static/img/galeria')
    alt = models.CharField(verbose_name="Texto Alternativo", max_length=100)
    data = models.DateTimeField(verbose_name="Data de publicação", auto_now=True)

    class Meta:
        verbose_name = "Galeria"
        db_table = 'galeria'

    def __str__(self):
        return self.alt
    