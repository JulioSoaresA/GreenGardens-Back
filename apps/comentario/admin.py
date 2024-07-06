from django.contrib import admin
from .models import Comentario, ImagemComentario

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'autor', 'texto', 'data_publicacao',)
    list_display_links = ('id', 'autor',)
    list_filter = ('autor', 'data_publicacao',)
    filter_horizontal = ()
    fieldsets = ()


class ImagemComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagem',)
    list_display_links = ('id', 'imagem',)
    list_filter = ('imagem',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Comentario, ComentarioAdmin)
admin.site.register(ImagemComentario, ImagemComentarioAdmin)
