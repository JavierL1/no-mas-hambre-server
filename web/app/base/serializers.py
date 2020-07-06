from rest_framework import serializers

from .models import Comuna, Lugar, Provincia, Region


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'
        read_only_fields = ['nombre', 'codigo', 'posicion', 'alias']


class ProvinciaSerializer(serializers.ModelSerializer):
    region = RegionSerializer()

    class Meta:
        model = Provincia
        fields = '__all__'
        read_only_fields = ['nombre', 'codigo', 'region']


class ComunaSerializer(serializers.ModelSerializer):
    provincia = ProvinciaSerializer(required=False)

    class Meta:
        model = Comuna
        fields = '__all__'
        read_only_fields = ['nombre', 'provincia']


class LugarSerializer(serializers.ModelSerializer):
    comuna = ComunaSerializer()

    class Meta:
        model = Lugar
        fields = ['localidad', 'comuna', 'direccion']

    def create(self, validated_data):
        comuna_data = validated_data.pop('comuna')
        comuna = Comuna.objects.get(codigo=comuna_data.get('codigo'))
        validated_data['comuna'] = comuna
        lugar = Lugar.objects.create(**validated_data)
        return lugar
