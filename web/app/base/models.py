from django.db import models

# Create your models here.


class Region(models.Model):
    class Meta:
        verbose_name = 'región'
        verbose_name_plural = 'regiones'

    nombre = models.CharField(verbose_name='nombre', max_length=64)
    codigo = models.IntegerField(verbose_name='código')
    posicion = models.IntegerField(verbose_name='posición', null=True)
    alias = models.CharField(verbose_name='alias', null=True, max_length=64)


class Provincia(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=64)
    codigo = models.IntegerField(verbose_name='código')
    region = models.ForeignKey(
        Region,
        verbose_name='región',
        on_delete=models.CASCADE,
        related_name='provincias'
    )


class Comuna(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=64)
    codigo = models.IntegerField(verbose_name='código')
    provincia = models.ForeignKey(
        Provincia,
        verbose_name='provincia',
        on_delete=models.CASCADE,
        related_name='comunas'
    )


class Lugar(models.Model):
    class Meta:
        verbose_name_plural = 'lugares'

    localidad = models.CharField(verbose_name='localidad', max_length=300)
    comuna = models.ForeignKey(
        Comuna,
        verbose_name='comuna',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='lugares'
    )
    direccion = models.CharField(
        verbose_name='direccion',
        max_length=300,
        blank=True,
        null=True
    )


class Persona(models.Model):
    nombre = models.CharField(verbose_name='nombre', max_length=64)
    apellido = models.CharField(
        verbose_name='apellido', max_length=64, null=True, blank=True
    )
    rut = models.IntegerField(verbose_name='rut', null=True, blank=True)
    dv = models.IntegerField(
        verbose_name='dígito verificador', null=True, blank=True
    )
    lugar = models.ForeignKey(
        Lugar,
        verbose_name='lugar',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='personas'
    )


class Contacto(models.Model):
    class TipoContacto(models.TextChoices):
        NO_ASIGNADA = 'NA'
        TELEFONO_MOVIL = 'TM'
        TELEFONO_FIJO = 'TF'
        FACEBOOK = 'FB'
        TWITTER = 'TW'
        INSTAGRAM = 'IG'
        LINKED_IN = 'LI'
        EMAIL = 'EM'


    tipo_contacto = models.CharField(
        verbose_name='tipo de contacto',
        max_length=2,
        choices=TipoContacto.choices,
        default=TipoContacto.NO_ASIGNADA
    )
    contenido = models.CharField(
        verbose_name='url/usuario/numero', max_length=300
    )
    persona = models.ForeignKey(
        Persona,
        verbose_name='persona',
        on_delete=models.CASCADE,
        related_name='contactos'
    )


class Organizacion(models.Model):
    class Meta:
        verbose_name = 'organización'
        verbose_name_plural = 'organizaciones'

    nombre = models.CharField('nombre', max_length=64)
    apellido = models.CharField(
        'apellido', max_length=64, null=True, blank=True
    )
    rut = models.IntegerField('rut', null=True, blank=True)
    dv = models.IntegerField('dv', null=True, blank=True)
    lugar = models.ForeignKey(
        Lugar,
        verbose_name='lugar',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='organizaciones'
    )


class Participante(models.Model):
    organizacion = models.ForeignKey(
        Organizacion,
        verbose_name='organización',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='org_participantes'
    )
    persona = models.ForeignKey(
        Persona,
        verbose_name='persona',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='per_participantes'
    )
    activo = models.BooleanField(verbose_name='activo', default=True)


class TipoGestion(models.Model):
    class Meta:
        verbose_name = 'tipo gestión'
        verbose_name_plural = 'tipos gestión'

    etiqueta = models.CharField('etiqueta', max_length=64)
