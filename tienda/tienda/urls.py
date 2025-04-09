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
    path ('formulario1/', views.crear_tiendas, name= 'crear_tiendas'),
    path ('productos/<int:pepito>/', views.dame_producto, name="dame_producto"),
    path ('productos/<int:juanito>/editar', views.editar_producto, name="editar_producto"),
    path ('tiendas/<int:pepito1>/', views.dame_tienda, name="dame_tienda"),
    path ('tiendas/<int:juanito1>/editar', views.editar_tienda, name="editar_tienda")
]
