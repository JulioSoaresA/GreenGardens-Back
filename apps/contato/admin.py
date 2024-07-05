from django.contrib import admin
from .models import Contato, ContatoFormulario

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'endereco', 'email',)
    list_display_links = ('id', 'endereco',)
    list_filter = ('endereco', 'email',)
    filter_horizontal = ()
    fieldsets = ()


class ContatoFormularioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email', 'mensagem',)
    list_display_links = ('id', 'nome',)
    list_filter = ('nome', 'email',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Contato, ContatoAdmin)
admin.site.register(ContatoFormulario, ContatoFormularioAdmin)
