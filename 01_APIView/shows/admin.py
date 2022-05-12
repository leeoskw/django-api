from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Banda)
class BandaAdmin(admin.ModelAdmin):
    fields = ('nome', 'em_atividade')

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display: '__all__'


@admin.register(Musica)
class MusicaAdmin(admin.ModelAdmin):
    list_display:  '__all__'


@admin.register(Integrante)
class IntegranteAdmin(admin.ModelAdmin):
    list_display: '__all__'