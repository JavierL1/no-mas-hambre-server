from rest_framework import serializers

from base import models


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
        comuna_data = validated_data.pop('comuna')
        comuna = models.Comuna.objects.get(codigo=comuna_data.get('codigo'))
        validated_data['comuna'] = comuna
        lugar = models.Lugar.objects.create(**validated_data)
        return lugar


class TipoContactoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoContacto
        fields = '__all__'
        extra_kwargs = {'nombre': {'validators': []}}


class ContactoSerializer(serializers.ModelSerializer):
    tipo = TipoContactoSerializer()

    class Meta:
        model = models.Contacto
        fields = ['contenido', 'tipo']

    def create(self, validated_data):
        tipo_data = validated_data.pop('tipo')
        tipo, _ = models.TipoContacto.objects \
            .get_or_create(
                nombre=tipo_data.get('nombre').lower(),
                defaults={'descripcion': tipo_data.get('descripcion')}
            )
        contacto = models.Contacto.objects.create(tipo=tipo, **validated_data)
        return contacto


class PersonaSerializer(serializers.ModelSerializer):
    lugar = LugarSerializer()
    contactos = ContactoSerializer(many=True)

    class Meta:
        model = models.Persona
        fields = '__all__'

    def create(self, validated_data):
        contactos_data = validated_data.pop('contactos')
        lugar_data = validated_data.pop('lugar')
        validated_data['lugar'] = LugarSerializer().create(lugar_data)
        persona = models.Persona.objects.create(**validated_data)
        for contacto_data in contactos_data:
            ContactoSerializer().create(
                {'persona': persona, **contacto_data}
            )
        return persona


class TipoOrganizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TipoOrganizacion
        fields = '__all__'
        extra_kwargs = {'nombre': {'validators': []}}


class OrganizacionSerializer(serializers.ModelSerializer):
    tipo = TipoOrganizacionSerializer()
    lugar = LugarSerializer()

    class Meta:
        model = models.Organizacion
        fields = '__all__'

    def create(self, validated_data):
        tipo_data = validated_data.pop('tipo')
        validated_data['tipo'], _ = models.TipoOrganizacion.objects \
            .get_or_create(
                nombre=tipo_data.get('nombre').lower(),
                defaults={'descripcion': tipo_data.get('descripcion')}
            )
        lugar_data = validated_data.pop('lugar')
        validated_data['lugar'] = LugarSerializer().create(lugar_data)
        return models.Organizacion.objects.create(**validated_data)
