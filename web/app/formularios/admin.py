from django.contrib import admin
from .models import Necesidad, AtencionNecesidad, EstadoAtencionNecesidad

# Register your models here.


@admin.register(Necesidad)
class NecesidadAdmin(admin.ModelAdmin):
    pass


@admin.register(AtencionNecesidad)
class AtencionNecesidadAdmin(admin.ModelAdmin):
    list_display = ['necesidad', 'estado_actual']
