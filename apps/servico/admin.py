from django.contrib import admin
from .models import Servico, NossosServicos

class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'imagem', 'titulo', 'alt',)
    list_display_links = ('id', 'imagem',)
    filter_horizontal = ()
    fieldsets = ()


class NossosServicosAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao',)
    list_display_links = ('id', 'titulo',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Servico, ServicoAdmin)
admin.site.register(NossosServicos, NossosServicosAdmin)
                    