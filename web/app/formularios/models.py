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
    fecha_insercion = models.DateTimeField(verbose_name='fecha de inserción')
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


class Voluntario(models.Model):
    fecha_insercion = models.DateTimeField(verbose_name='fecha de inserción')
    remitente = models.ForeignKey(
        Participante,
        verbose_name='remitente',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='voluntarios'
    )
    descripcion = models.CharField(verbose_name='descripción', max_length=300)


class Ayuda(models.Model):
    nombre = models.CharField('nombre', max_length=64)
    fecha_insercion = models.DateTimeField(verbose_name='fecha de inserción')
    remitente = models.ForeignKey(
        Participante,
        verbose_name='remitente',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='ayudas'
    )
    tipo_gestion = models.ForeignKey(
        TipoGestion,
        verbose_name='tipo de gestión',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='ayudas'
    )
    lugar = models.ForeignKey(
        Lugar,
        verbose_name='lugar',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='ayudas'
    )
    descripcion = models.CharField(verbose_name='descripción', max_length=300)
    rango = models.FloatField(verbose_name='rango')
    activo = models.BooleanField(verbose_name='activo')


class Accion(models.Model):
    nombre = models.CharField('nombre', max_length=64)


class Evento(models.Model):
    necesidad = models.ForeignKey(
        Necesidad,
        verbose_name='necesidad',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='eventos'
    )
    proveedor = models.ForeignKey(
        Proveedor,
        verbose_name='proveedor',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='eventos'
    )
    voluntario = models.ForeignKey(
        Voluntario,
        verbose_name='voluntario',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='eventos'
    )
    ayuda = models.ForeignKey(
        Ayuda,
        verbose_name='ayuda',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='eventos'
    )
    lugar = models.ForeignKey(
        Lugar,
        verbose_name='lugar',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='eventos'
    )
    fecha = models.DateTimeField(verbose_name='fecha')
    descripcion = models.CharField(verbose_name='descripción', max_length=300)
    accion = models.ForeignKey(
        Accion,
        verbose_name='acción',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='eventos'
    )
