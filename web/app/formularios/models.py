from django.db import models
from base.models import Lugar, Persona

# Create your models here.


class Necesidad(models.Model):
    class Meta:
        verbose_name_plural = "necesidades"

    dt_insercion = models.DateTimeField('fecha insercion')
    remitente = models.ForeignKey(
        Persona,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='necesidades_ingresadas'
    )
    ayudado = models.ForeignKey(
        Persona,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='necesidades'
    )
    lugar = models.ForeignKey(
        Lugar,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='necesidades_ubicadas'
    )
    descripcion = models.CharField('descripción', max_length=300)
