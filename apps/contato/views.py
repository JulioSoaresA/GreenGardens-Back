from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContatoForm

def contato(request):
    if request.method == "GET":
        form = ContatoForm()
        return render(request, 'contato/contato.html', locals())
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            email = form.cleaned_data['email']
            contato = form.save()
            send_mail(
                assunto,
                mensagem,
                email,
                ['juliocsoaresa1@gmail.com'])

            form = ContatoForm()
            messages.success(request, 'Cadastro realizado com sucesso')
        return render(request, 'contato/contato.html', locals())