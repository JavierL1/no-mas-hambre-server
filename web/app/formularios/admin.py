from django.contrib import admin
from .models import Necesidad

# Register your models here.


@admin.register(Necesidad)
class NecesidadAdmin(admin.ModelAdmin):
    pass
