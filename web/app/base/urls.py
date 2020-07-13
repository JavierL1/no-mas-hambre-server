# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'comunas', views.ComunaViewSet)
router.register(r'lugares', views.LugarViewSet)
router.register(r'personas', views.PersonaViewSet)
router.register(r'organizaciones', views.OrganizacionViewSet)
router.register(r'participantes', views.ParticipanteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    )
]
