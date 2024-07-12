from django.contrib import admin
from .models import NossosEbooks, Ebook


class NossosEbooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao',)
    list_display_links = ('id', 'titulo',)
    list_filter = ('titulo', 'descricao',)
    filter_horizontal = ()
    fieldsets = ()


class EbookAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'arquivo', 'imagem', 'data_publicacao',)
    list_display_links = ('id', 'titulo',)
    list_filter = ('titulo', 'descricao', 'arquivo', 'imagem', 'data_publicacao',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(NossosEbooks, NossosEbooksAdmin)
admin.site.register(Ebook, EbookAdmin)
