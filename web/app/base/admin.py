from django.contrib import admin
from .models import Comuna, Contacto, Lugar, Organizacion, Participante
from .models import Persona, Provincia, Region, TipoGestion

# Register your models here.

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', )


@admin.register(Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', )


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', )


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    pass


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass


@admin.register(Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    pass


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoGestion)
class TipoGestionAdmin(admin.ModelAdmin):
    pass
