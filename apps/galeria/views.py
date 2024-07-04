from django.shortcuts import render
from apps.sobre.models import Intro, NossosValores, Valores


def index(request):
    intro = Intro.objects.all().order_by('-id')
    nossos_valores = NossosValores.objects.all().last()
    valores = Valores.objects.all().order_by('-id')
    return render(request, 'index.html', locals())
