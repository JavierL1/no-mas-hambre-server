from django.contrib import admin
from .models import Comuna, Contacto, Lugar, Persona, Region, TipoContacto

# Register your models here.


@admin.register(Comuna)
class ComunaAdmin(admin.ModelAdmin):
    pass


@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    pass


@admin.register(Lugar)
class LugarAdmin(admin.ModelAdmin):
    pass


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    pass


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    pass


@admin.register(TipoContacto)
class TipoContactoAdmin(admin.ModelAdmin):
    pass
