from django.shortcuts import render
from apps.sobre.models import Intro


def index(request):
    intro = Intro.objects.all().order_by('-id')
    return render(request, 'index.html', locals())
