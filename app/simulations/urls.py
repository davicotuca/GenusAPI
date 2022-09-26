from django.urls import path
# from app.simulations.views import derivaGargalo

from simulations import views


app_name = 'simulations'

urlpatterns = [
    path('deriva/', views.deriva),
    path('derivaGargalo/', views.derivaGargalo),
    path('selecao/', views.selecao)
]
