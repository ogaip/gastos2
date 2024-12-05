from django.contrib import admin
from .models import Perfil, CustomUser

# Register your models here.

class PerfilAdmin(admin.ModelAdmin):
    model = Perfil
    list_display = ['user', 'profesion', 'puesto_actual', 'empresa', 'telefono', 'direccion', 'ciudad', 'estado', 'pais', 'codigo_postal', 'fecha_nacimiento', 'genero', 'foto', 'curriculum']

    
admin.site.register(Perfil, PerfilAdmin)
admin.site.register(CustomUser)
