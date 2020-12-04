from django.contrib import admin
from django.urls import path, include
from lavajato.views import ClientesViewSet, VeiculosViewSet, RevisaoViewSet,ListaRevisaoClienteViewSet, ListaClientesVeiculosRevisaosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('clientes', ClientesViewSet)
router.register('veiculos', VeiculosViewSet)
router.register('revisaos', RevisaoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('cliente/<int:pk>/revisaos/', ListaRevisaoClienteViewSet.as_view()),
    path('veiculo/<int:pk>/revisaos/', ListaClientesVeiculosRevisaosViewSet.as_view())
]

