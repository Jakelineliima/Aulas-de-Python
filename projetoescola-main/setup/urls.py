from django.contrib import admin
from django.urls import path, include
from escola.views import ClientesViewSet, VeiculosViewSet, RevisaoViewSet, ListaRevisaoClienteSerializer, ListaClientesRevisaoSerializer

from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)
router.register('veiculos', VeiculosViewSet)
router.register('revisaos', RevisaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/revisao/', ListaRevisaoClienteSerializer.as_view()),
    path('cliente/<int:pk>/revisao/',  ListaClientesRevisaoSerializer.as_view())
]
