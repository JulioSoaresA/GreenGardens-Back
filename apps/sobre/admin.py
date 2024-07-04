from django.contrib import admin
from .models import Intro


class IntroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo',)
    list_display_links = ('id', 'titulo',)
    list_filter = ('titulo',)
    filter_horizontal = ()
    fieldsets = ()


admin.site.register(Intro, IntroAdmin)
