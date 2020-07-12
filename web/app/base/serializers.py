import logging

from rest_framework import serializers

from base import models


logger = logging.getLogger(__name__)


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = '__all__'
        read_only_fields = ['nombre', 'codigo', 'posicion', 'alias']


class ProvinciaSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = models.Provincia
        fields = '__all__'
        read_only_fields = ['nombre', 'codigo', 'region']


class ComunaSerializer(serializers.ModelSerializer):
    provincia = ProvinciaSerializer(required=False)

    class Meta:
        model = models.Comuna
        fields = '__all__'
        read_only_fields = ['nombre', 'provincia']


class LugarSerializer(serializers.ModelSerializer):
    comuna = ComunaSerializer()

    class Meta:
        model = models.Lugar
        fields = ['localidad', 'comuna', 'direccion']

    def create(self, validated_data):
        logger.error(validated_data)
        comuna_data = validated_data.pop('comuna')
        comuna = models.Comuna.objects.get(codigo=comuna_data.get('codigo'))
        validated_data['comuna'] = comuna
        lugar = models.Lugar.objects.create(**validated_data)
        return lugar


class TipoContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoContacto
        fields = ['nombre', 'descripcion']


class ContactoSerializer(serializers.ModelSerializer):
    tipo = TipoContactoSerializer()

    class Meta:
        model = models.Contacto
        fields = ['contenido', 'tipo']

    def create(self, validated_data):
        logger.error(validated_data)
        tipo_data = validated_data.pop('tipo')
        tipo, _ = models.TipoContacto.objects \
            .get_or_create(nombre=tipo_data.get('nombre'))
        contacto = models.Contacto.objects.create(tipo=tipo, **validated_data)
        return contacto


class PersonaSerializer(serializers.ModelSerializer):
    lugar = LugarSerializer()
    contactos = ContactoSerializer(many=True)

    class Meta:
        model = models.Persona
        fields = '__all__'

    def create(self, validated_data):
        logger.error(validated_data)
        contactos_data = validated_data.pop('contactos')
        lugar_data = validated_data.pop('lugar')
        validated_data['lugar'] = LugarSerializer().create(lugar_data)
        persona = models.Persona.objects.create(**validated_data)
        for contacto_data in contactos_data:
            ContactoSerializer().create(
                {'persona': persona, **contacto_data}
            )
        return persona
