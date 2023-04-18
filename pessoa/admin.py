from django.contrib import admin
from .models import Sobrevivente

@admin.register(Sobrevivente)
class SobreviventeAdmin(admin.ModelAdmin):
    list_display = ( 'nome', 'idade', 'sexo', 'pontos', 'denuncias', 'localizacao', 'infectado')
    list_editable = ('denuncias', 'localizacao')
