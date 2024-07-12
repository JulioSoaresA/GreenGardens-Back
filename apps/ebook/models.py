from django.db import models


class NossosEbooks(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
    

class Ebook(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=100)
    descricao = models.TextField()
    arquivo = models.FileField(verbose_name="Arquivo", upload_to='core/static/ebook')
    imagem = models.ImageField(verbose_name="Imagem", upload_to='core/static/img/ebook')
    data_publicacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Ebook'
        verbose_name_plural = 'Ebooks'
        db_table = 'ebook'

    def __str__(self):
        return self.titulo
    

class CadastroEbook(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=100)
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    email = models.EmailField(verbose_name="Email", max_length=100)
    ebook = models.ForeignKey(Ebook, on_delete=models.CASCADE, verbose_name="Ebook")

    class Meta:
        verbose_name = 'Cadastro Ebook'
        verbose_name_plural = 'Cadastro Ebooks'
        db_table = 'cadastro_ebook'

    def __str__(self):
        return self.nome
