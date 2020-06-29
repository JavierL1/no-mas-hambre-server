from django.db import models
from base.models import Lugar, Participante, TipoGestion

# Create your models here.


class Periodicidad(models.Model):
    class Meta:
        verbose_name = 'periodicidad'
        verbose_name_plural = 'periodicidades'

    nombre = models.CharField(
        'nombre', max_length=64, unique=True, null=False, blank=False
    )
    descripcion = models.CharField(
        'descripción', max_length=300, null=True, blank=True
    )


class EstadoNecesidad(models.Model):
    class Meta:
        verbose_name = 'estado de necesidad'
        verbose_name_plural = 'estados de necesidad'

    nombre = models.CharField(
        'nombre', max_length=64, unique=True, null=False, blank=False
    )
    descripcion = models.CharField(
        'descripción', max_length=300, null=True, blank=True
    )


class AlimentacionEspecial(models.Model):
    class Meta:
        verbose_name = 'alimentación especial'
        verbose_name_plural = 'alimentaciones especiales'

    nombre = models.CharField(
        'nombre', max_length=64, unique=True, null=False, blank=False
    )
    descripcion = models.CharField(
        'descripción', max_length=300, null=True, blank=True
    )


class Necesidad(models.Model):
    class Meta:
        verbose_name_plural = 'necesidades'

        def __str__(self):
            return self.descripcion

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
    periodicidad = models.ForeignKey(
        Periodicidad,
        verbose_name='periodicidad',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='necesidades'
    )
    descripcion = models.CharField(verbose_name='descripción', max_length=1024)
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
    estado = models.ForeignKey(
        EstadoNecesidad,
        verbose_name='estado de necesidad',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='necesidades'
    )
    cantidad_menores = models.IntegerField(
        'cantidad de menores', null=True, blank=True
    )
    cantidad_adultos = models.IntegerField(
        'cantidad de adultos', null=True, blank=True
    )
    cantidad_mayores = models.IntegerField(
        'cantidad de mayores', null=True, blank=True
    )
    alimentacion_especial = models.ForeignKey(
        AlimentacionEspecial,
        verbose_name='alimentación especial',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='necesidades'
    )


class Proveedor(models.Model):
    fecha_insercion = models.DateTimeField(verbose_name='fecha de inserción')
    tipos_gestion = models.ManyToManyField(
        TipoGestion,
        verbose_name='tipos de gestión',
        related_name='proveedores'
    )
    despacho = models.BooleanField(verbose_name='despacho', null=True)
    retiro = models.BooleanField(verbose_name='retiro', null=True)
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
    descripcion = models.CharField(verbose_name='descripción', max_length=1024)
    rango = models.FloatField(verbose_name='rango', null=True)
    alcance = models.CharField(verbose_name='alcance', max_length=64, null=True)
    activo = models.BooleanField(verbose_name='activo')
    mayorista = models.BooleanField(verbose_name='mayorista', null=True)
    minorista = models.BooleanField(verbose_name='minorista', null=True)


class TipoVoluntario(models.Model):
    class Meta:
        verbose_name = 'tipo de voluntario'
        verbose_name_plural = 'tipos de voluntario'

    categoria = models.CharField(
        'categoría', max_length=128, null=False, blank=False
    )
    nombre = models.CharField(
        'nombre', max_length=128, unique=True, null=False, blank=False
    )
    descripcion = models.CharField(
        'descripción', max_length=300, null=True, blank=True
    )


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
    descripcion = models.CharField(verbose_name='descripción', max_length=1024)
    periodicidad = models.ForeignKey(
        Periodicidad,
        verbose_name='periodicidad',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='voluntarios'
    )
    tipos = models.ManyToManyField(
        TipoVoluntario,
        verbose_name='tipo de voluntario',
        related_name='voluntarios'
    )


class TipoAyuda(models.Model):
    class Meta:
        verbose_name = 'tipo de ayuda'
        verbose_name_plural = 'tipos de ayuda'

    categoria = models.CharField(
        'categoría', max_length=128, null=False, blank=False
    )
    nombre = models.CharField(
        'nombre', max_length=128, unique=True, null=False, blank=False
    )
    descripcion = models.CharField(
        'descripción', max_length=300, null=True, blank=True
    )


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
    descripcion = models.CharField(verbose_name='descripción', max_length=1024)
    rango = models.FloatField(verbose_name='rango')
    activo = models.BooleanField(verbose_name='activo')
    periodicidad = models.ForeignKey(
        Periodicidad,
        verbose_name='periodicidad',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='ayudas'
    )
    tiene_estimado = models.BooleanField(
        verbose_name='tiene estimado de personas que ayuda', null=True, blank=True
    )
    tiene_material = models.BooleanField(
        verbose_name='tiene material audiovisual', null=True, blank=True
    )
    tiene_descripcion = models.BooleanField(
        verbose_name='tiene descripción', null=True, blank=True
    )
    tipos = models.ManyToManyField(
        TipoAyuda,
        verbose_name='tipos de ayuda',
        related_name='ayudas'
    )


class Accion(models.Model):
    nombre = models.CharField('nombre', max_length=64)
    descripcion = models.CharField('descripción', max_length=300)


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
    descripcion = models.CharField(verbose_name='descripción', max_length=1024)
    accion = models.ForeignKey(
        Accion,
        verbose_name='acción',
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name='eventos'
    )
