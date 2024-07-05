from django.db import models


class ContatoFormulario(models.Model):
    nome = models.CharField(verbose_name="Nome", max_length=150)
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    email = models.EmailField(verbose_name="Email", max_length=200)
    mensagem = models.TextField(verbose_name="Mensagem", max_length=255)

    class Meta:
        verbose_name = "Contato"
        db_table = 'contato'

    def __str__(self):
        return self.nome


class Contato(models.Model):
    endereco = models.CharField(verbose_name="Endereço", max_length=150)
    email = models.EmailField(verbose_name="Email", max_length=200)
    telefone = models.CharField(verbose_name="Telefone", max_length=15)
    link_maps = models.TextField(verbose_name="Link do Google Maps")
    instagram = models.CharField(verbose_name="Instagram", max_length=150)
    facebook = models.CharField(verbose_name="Facebook", max_length=150)

    class Meta:
        verbose_name = "Nosso contato"
        db_table = 'nosso_contato'

    def __str__(self):
        return self.endereco
