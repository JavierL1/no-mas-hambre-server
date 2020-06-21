from django.db import models
from base.models import Lugar, Participante, TipoGestion

# Create your models here.


class Necesidad(models.Model):
    class Meta:
        verbose_name_plural = 'necesidades'

        def __str__(self):
            return self.descripcion

    class EstadoNecesidad(models.TextChoices):
        PENDIENTE = 'PE'
        ASIGNADA = 'AS'
        RESUELTA = 'RE'

    fecha_insercion = models.DateTimeField(verbose_name='fecha de inserción')
    remitente = models.ForeignKey(
        Participante,
        verbose_name='remitente',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='necesidades_ingresadas'
    )
    ayudado = models.ForeignKey(
        Participante,
        verbose_name='ayudado',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='necesidades'
    )
    lugar = models.ForeignKey(
        Lugar,
        verbose_name='lugar',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='necesidades'
    )
    periodicidad = models.CharField(
        verbose_name='periodicidad', max_length=300
    )
    descripcion = models.CharField(verbose_name='descripción', max_length=300)
    fecha_finalizacion = models.DateTimeField(
        verbose_name='fecha de finalización',
        blank=True,
        null=True
    )
    tipo_gestion = models.ForeignKey(
        TipoGestion,
        verbose_name='tipo de gestión',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='necesidades'
    )
    estado = models.CharField(
        verbose_name='estado',
        max_length=2,
        choices=EstadoNecesidad.choices,
        default=EstadoNecesidad.PENDIENTE
    )


class Proveedor(models.Model):
    tipos_gestion = models.ManyToManyField(
        TipoGestion,
        verbose_name='tipos de gestión',
        related_name='proveedores'
    )
    despacho = models.BooleanField(verbose_name='despacho')
    remitente = models.ForeignKey(
        Participante,
        verbose_name='remitente',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='proveedores'
    )
    lugar = models.ForeignKey(
        Lugar,
        verbose_name='lugar',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='proveedores'
    )
    descripcion = models.CharField(verbose_name='descripción', max_length=300)
    rango = models.FloatField(verbose_name='rango')
    activo = models.BooleanField(verbose_name='activo')
