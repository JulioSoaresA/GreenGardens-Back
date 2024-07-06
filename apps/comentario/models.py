from django.db import models

class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    texto = models.TextField()
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        db_table = 'comentario'

    def __str__(self):
        return self.autor
    

class ImagemComentario(models.Model):
    imagem = models.ImageField(verbose_name="Imagem", upload_to='core/static/img/comentario')

    class Meta:
        verbose_name = "Imagem do Comentário"
        db_table = 'imagem_comentario'

    def __str__(self):
        return self.imagem.url
