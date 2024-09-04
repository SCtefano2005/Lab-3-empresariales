from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_historial, name='index_historial'),
    path('registrar-entrada/', views.registrar_entrada, name='registrar_entrada'),
    path('registrar-salida/', views.registrar_salida, name='registrar_salida'),
    path('salida-exitosa/<str:codigo>/', views.salida_exitosa, name='salida_exitosa'),
]
