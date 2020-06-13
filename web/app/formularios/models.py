from django.db import models
from base.models import Lugar, Persona

# Create your models here.


class Necesidad(models.Model):
    class Meta:
        verbose_name_plural = 'necesidades'

        def __str__(self):
            return self.descripcion

    fecha_insercion = models.DateTimeField('fecha insercion')
    remitente = models.ForeignKey(
        Persona,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='necesidades_ingresadas'
    )
    ayudado = models.ForeignKey(
        Persona,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='necesidades'
    )
    lugar = models.ForeignKey(
        Lugar,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='necesidades_ubicadas'
    )
    descripcion = models.CharField('descripción', max_length=300)


class EstadoAtencionNecesidad(models.Model):
    class Meta:
        verbose_name_plural = 'estados atencion necesidad'



class AtencionNecesidad(models.Model):
    class Meta:
        verbose_name_plural = 'atenciones necesidad'

    class Estados(models.TextChoices):
        NO_ASIGNADA = 'NA'
        ASIGNADA = 'A'
        FINALIZADA = 'F'

    necesidad = models.ForeignKey(
        Necesidad,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='atenciones'
    )
    fecha_ingreso = models.DateTimeField('fecha ingreso')
    fecha_objetivo = models.DateTimeField('fecha objetivo')
    fecha_asignacion = models.DateTimeField(
        'fecha asignacion',
        blank=True,
        null=True,
    )
    fecha_finalizacion = models.DateTimeField(
        'fecha finalizacion',
        blank=True,
        null=True,
    )
    estado_actual = models.CharField(
        max_length=2,
        choices=Estados.choices,
        default=Estados.NO_ASIGNADA,
    )
