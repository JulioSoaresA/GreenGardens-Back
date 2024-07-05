from django.contrib import admin
from .models import Galeria

class GaleriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagem', 'alt', 'data',)
    list_display_links = ('id', 'imagem',)
    list_filter = ('data',)
    filter_horizontal = ()
    fieldsets = ()

admin.site.register(Galeria, GaleriaAdmin)
