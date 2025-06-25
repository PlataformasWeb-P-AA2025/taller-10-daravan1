from django.urls import path
# se importa las vistas de la aplicación
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Esta ruta corresponde a /ordenamiento/
    path('parroquias/', views.listar_parroquia, name='listar_parroquia'),
    path('barrios/', views.listar_barrio, name='listar_barrio'),
    path('agregar_barrio/', views.agregar_barrio, name='agregar_barrio'),
    path('agregar_parroquias', views.agregar_parroquia, name='agregar_parroquia'),
]