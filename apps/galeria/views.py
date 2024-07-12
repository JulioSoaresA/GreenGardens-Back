from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
import mimetypes

from .models import Galeria
from apps.sobre.models import Intro, NossosValores, Valores, QuemSomos, ImagemQuemSomos
from apps.servico.models import Servico, NossosServicos
from apps.ebook.models import NossosEbooks, Ebook, CadastroEbook
from apps.contato.models import Contato
from apps.comentario.models import Comentario, ImagemComentario
from apps.contato.forms import ContatoForm


def index(request):
    intro = Intro.objects.all().order_by('-id')
    quem_somos = QuemSomos.objects.all().first()
    imagem_quem_somos = ImagemQuemSomos.objects.all().first()
    servicos = Servico.objects.all().order_by('-id')
    nossos_servicos = NossosServicos.objects.all().first()
    nossos_ebooks = NossosEbooks.objects.all().first()
    ebook = Ebook.objects.all().first()
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


def processa_ebook_form(request, ebook_id):
    if request.method == 'POST':
        nome = request.POST.get('modalName')
        telefone = request.POST.get('modalTelefone')
        email = request.POST.get('modalEmail')

        ebook = get_object_or_404(Ebook, pk=ebook_id)

        # Salvar os dados no modelo CadastroEbook
        cadastro = CadastroEbook(
            nome=nome,
            telefone=telefone,
            email=email,
            ebook=ebook
        )
        cadastro.save()

        # Retornar a URL de download do ebook
        download_url = f'/download/{ebook_id}/'
        return JsonResponse({'success': True, 'download_url': download_url})

    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)


def download_ebook(request, ebook_id):
    print('download_ebook')
    if request.method == 'POST':
        nome = request.POST.get('modalName')
        telefone = request.POST.get('modalTelefone')
        email = request.POST.get('modalEmail')

        ebook = get_object_or_404(Ebook, pk=ebook_id)

        errors = {}

        # Verificar se o e-mail já está cadastrado
        if CadastroEbook.objects.filter(email=email).exists():
            errors['email'] = ['E-mail já cadastrado.']

        # Verificar se o telefone já está cadastrado
        if CadastroEbook.objects.filter(telefone=telefone).exists():
            errors['telefone'] = ['Número de telefone já cadastrado.']

        if errors:
            return JsonResponse({'success': False, 'errors': errors}, status=400)

        # Salvar os dados no modelo CadastroEbook
        cadastro = CadastroEbook(
            nome=nome,
            telefone=telefone,
            email=email,
            ebook=ebook
        )
        cadastro.save()

        # Preparar a URL do arquivo para download
        file_path = ebook.arquivo.url  # Use .url instead of .path

        response_data = {
            'success': True,
            'download_url': file_path
        }

        return JsonResponse(response_data)

    return JsonResponse({'success': False, 'error': 'Método não permitido'}, status=405)