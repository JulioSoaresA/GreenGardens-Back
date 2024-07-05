from django.shortcuts import render
from django.core.mail import send_mail
from apps.sobre.models import Intro, NossosValores, Valores
from apps.contato.models import Contato
from apps.contato.forms import ContatoForm


def index(request):
    intro = Intro.objects.all().order_by('-id')
    nossos_valores = NossosValores.objects.all().last()
    valores = Valores.objects.all().order_by('-id')
    contato = Contato.objects.all().last()

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
