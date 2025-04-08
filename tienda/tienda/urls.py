from django.urls import path, include
from . import views

urlpatterns = [
    path ('',views.index, name = 'inicio'),
    path ('clientes/', views.lista_clientes, name= 'lista_clientes'),
    path ('registrar', views.registrar_usuario, name='registrar_usuario'),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('vendedores/', views.lista_vendedores, name= 'lista_vendedores'),
    path ('productos/', views.lista_productos, name= 'lista_productos'),
    path ('formulario/', views.crear_productos, name= 'crear_productos'),
    path ('tiendas/', views.lista_tiendas, name= 'lista_tiendas'),
    path ('crear_tienda/', views.crear_tienda, name= 'crear_tienda'),
]
