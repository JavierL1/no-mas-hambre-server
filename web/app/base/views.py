from rest_framework import viewsets

from base import serializers
from base import models


class ComunaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Comuna.objects.all().order_by('nombre')
    serializer_class = serializers.ComunaSerializer


class LugarViewSet(viewsets.ModelViewSet):
    queryset = models.Lugar.objects.all().order_by('comuna__nombre')
    serializer_class = serializers.LugarSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
