from django.urls import path

from simulations import views


app_name = 'simulations'

urlpatterns = [
    path('deriva/', views.deriva)
]
