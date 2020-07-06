from rest_framework import viewsets

from .serializers import ComunaSerializer, LugarSerializer
from .models import Comuna, Lugar


class ComunaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Comuna.objects.all().order_by('nombre')
    serializer_class = ComunaSerializer


class LugarViewSet(viewsets.ModelViewSet):
    queryset = Lugar.objects.all().order_by('comuna__nombre')
    serializer_class = LugarSerializer
