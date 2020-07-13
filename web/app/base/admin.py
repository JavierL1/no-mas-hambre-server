from django.contrib import admin
from base import models

# Register your models here.


@admin.register(models.Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', )


@admin.register(models.Provincia)
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', )


@admin.register(models.Comuna)
class ComunaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', )


@admin.register(models.Lugar)
class LugarAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Organizacion)
class OrganizacionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TipoGestion)
class TipoGestionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TipoContacto)
class TipoContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', )
    pass


@admin.register(models.TipoOrganizacion)
class TipoOrganizacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', )
    pass
