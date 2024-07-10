from django.shortcuts import render
from django.core.mail import send_mail
from .models import Galeria
from apps.sobre.models import Intro, NossosValores, Valores, QuemSomos, ImagemQuemSomos
from apps.servico.models import Servico, NossosServicos
from apps.contato.models import Contato
from apps.comentario.models import Comentario, ImagemComentario
from apps.contato.forms import ContatoForm


def index(request):
    intro = Intro.objects.all().order_by('-id')
    quem_somos = QuemSomos.objects.all().first()
    imagem_quem_somos = ImagemQuemSomos.objects.all().first()
    servicos = Servico.objects.all().order_by('-id')
    nossos_servicos = NossosServicos.objects.all().first()
    nossos_valores = NossosValores.objects.all().first()
    valores = Valores.objects.all().order_by('-id')
    galeria = Galeria.objects.all().order_by('-data')
    contato = Contato.objects.all().first()
    comentario = Comentario.objects.all().order_by('-data_publicacao').first()
    imagem_comentario = ImagemComentario.objects.first()

    if request.method == "GET":
        form = ContatoForm()
        return render(request, 'index.html', locals())
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            mensagem = form.cleaned_data['mensagem']
            email = form.cleaned_data['email']
            telefone = form.cleaned_data['telefone']
            contato = form.save()
            send_mail(
                f'{nome} - {telefone} - {email}',
                mensagem,
                email,
                ['juliocsoaresa1@gmail.com'])

            form = ContatoForm()
    return render(request, 'index.html', locals())
