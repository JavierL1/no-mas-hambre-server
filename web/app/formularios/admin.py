from django.contrib import admin
from .models import Accion, Ayuda, Evento, Necesidad, Proveedor, Voluntario

# Register your models here.


@admin.register(Accion)
class AccionAdmin(admin.ModelAdmin):
    pass


@admin.register(Ayuda)
class AyudaAdmin(admin.ModelAdmin):
    pass


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    pass


@admin.register(Necesidad)
class NecesidadAdmin(admin.ModelAdmin):
    pass


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    pass


@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    pass
