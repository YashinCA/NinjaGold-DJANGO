from django.urls import path
from . import views

app_name = 'presentacion'

urlpatterns = [
    path('', views.bienvenido, name='index'),
]
