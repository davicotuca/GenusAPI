from django.urls import (
    path,
    include,
)
# from app.simulations.views import derivaGargalo

from simulations import views

from rest_framework.routers import DefaultRouter

app_name = 'simulations'

router = DefaultRouter()
router.register('grupos', views.GrupoViewSet)
router.register('grupoSimulacao', views.GrupoSimulacaoViewSet)
# router.register('simulacao', views.SimulacaoViewSet)


urlpatterns = [
    # path('deriva/', views.deriva),
    # path('derivaGargalo/', views.derivaGargalo),
    # path('selecao/', views.selecao),
    # path('selecaoDeriva/', views.selecaoDeriva),
    path('simulator/', views.simulacaoGeral),
    # path('simulacaeeo/', views.simulacao),
    path('', include(router.urls)),
]
