from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
     path('usuarios/<int:id>/', usuario_detail, name='usuario_detail'),
    path('carros/<int:id>/', carro_detail, name='carro_detail'),
    path('registrar-usuario/', registrar_usuario, name='registrar_usuario'),
    path('registrar-carro/', registrar_carro, name='registrar_carro'),
    path('editar_usuario/<int:id>/', editar_usuario, name='editar_usuario'),
    path('editar_carro/<int:id>/', editar_carro, name='editar_carro'),
    path('listar_usuarios/', listar_usuarios, name='listar_usuarios'),
    path('listar_carros/', listar_carros, name='listar_carros'),
    path('eliminar_usuario/<int:id>/', eliminar_usuario, name='eliminar_usuario'),
    path('eliminar_carro/<int:id>/', eliminar_carro, name='eliminar_carro'),
]
