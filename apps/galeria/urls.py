from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('processa_ebook_form/<int:ebook_id>/', views.processa_ebook_form, name='processa_ebook_form'),
    path('download/<int:ebook_id>/', views.download_ebook, name='download_ebook'),
]