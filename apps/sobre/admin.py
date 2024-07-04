from django.contrib import admin
from .models import Intro, NossosValores, Valores


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


admin.site.register(Intro, IntroAdmin)
admin.site.register(NossosValores, NossosValoresAdmin)
admin.site.register(Valores, ValoresAdmin)
