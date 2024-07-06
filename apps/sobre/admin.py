from django.contrib import admin
from .models import Intro, NossosValores, Valores, QuemSomos, ImagemQuemSomos


class QuemSomosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao',)
    list_display_links = ('id', 'descricao',)
    list_filter = ('descricao',)
    filter_horizontal = ()
    fieldsets = ()


class ImagemQuemSomosAdmin(admin.ModelAdmin):
    list_display = ('id', 'alt',)
    list_display_links = ('id', 'alt',)
    list_filter = ('alt',)
    filter_horizontal = ()
    fieldsets = ()


class IntroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)
    list_display_links = ('id', 'titulo',)
    list_filter = ('titulo',)
    filter_horizontal = ()
    fieldsets = ()


class NossosValoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)
    list_display_links = ('id', 'titulo',)
    list_filter = ('titulo',)
    filter_horizontal = ()
    fieldsets = ()


class ValoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)
    list_display_links = ('id', 'titulo',)
    list_filter = ('titulo',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(QuemSomos, QuemSomosAdmin)
admin.site.register(ImagemQuemSomos, ImagemQuemSomosAdmin)
admin.site.register(Intro, IntroAdmin)
admin.site.register(NossosValores, NossosValoresAdmin)
admin.site.register(Valores, ValoresAdmin)
