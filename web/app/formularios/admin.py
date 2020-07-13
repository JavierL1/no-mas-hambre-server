from django.contrib import admin
from .models import Accion, Ayuda, Evento, Necesidad, Proveedor, Voluntario

# Register your models here.

MAX_DESCRIPTION_LENGTH = 100


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
    list_display = (
        'fecha_insercion', 'get_descripcion', 'get_comuna_nombre'
    )

    def get_descripcion(self, obj):
        if not obj.descripcion:
            return 'Sin descripción'
        if len(obj.descripcion) > MAX_DESCRIPTION_LENGTH:
            return obj.descripcion[:MAX_DESCRIPTION_LENGTH]
        else:
            return obj.descripcion

    get_descripcion.short_description = 'Descripción'

    def get_comuna_nombre(self, obj):
        if obj.lugar and obj.lugar.comuna:
            return obj.lugar.comuna.nombre.capitalize()
        else:
            return 'Sin comuna'

    get_comuna_nombre.short_description = 'Comuna'
    get_comuna_nombre.admin_order_field = 'lugar__comuna__nombre'


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    pass


@admin.register(Voluntario)
class VoluntarioAdmin(admin.ModelAdmin):
    pass
