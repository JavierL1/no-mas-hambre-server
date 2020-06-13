from django.db import models

# Create your models here.


class Persona(models.Model):
    nombre = models.CharField('nombre', max_length=64)
    apellido = models.CharField('apellido', max_length=64)


class TipoContacto(models.Model):
    class Meta:
        verbose_name_plural = 'tipos contacto'

    nombre = models.CharField('nombre', max_length=64)


class Contacto(models.Model):
    tipo_contacto = models.ForeignKey(
        TipoContacto,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='contactos'
    )
    contenido = models.CharField('url/usuario/numero', max_length=300)
    persona = models.ForeignKey(
        Persona,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='contactos'
    )


class Region(models.Model):
    class Meta:
        verbose_name_plural = 'regiones'

    nombre = models.CharField('nombre', max_length=64)
    codigo = models.IntegerField('código')
    posicion = models.IntegerField('posición')
    alias = models.CharField('alias', max_length=64)


class Comuna(models.Model):
    nombre = models.CharField('nombre', max_length=64)
    codigo = models.IntegerField('código')
    region = models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='comunas'
    )


class Lugar(models.Model):
    class Meta:
        verbose_name_plural = 'lugares'

    localidad = models.CharField('localidad', max_length=300)
    comuna = models.ForeignKey(
        Comuna,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='lugares'
    )
    direccion = models.CharField(
        'direccion',
        max_length=300,
        blank=True,
        null=True
    )
