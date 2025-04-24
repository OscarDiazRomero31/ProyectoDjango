from django.urls import path, include
from . import views

urlpatterns = [
    path ('',views.index, name = 'inicio'),
    path ('clientes/', views.lista_clientes, name= 'lista_clientes'),
    path ('registrar', views.registrar_usuario, name='registrar_usuario'),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('vendedores/', views.lista_vendedores, name= 'lista_vendedores'),
    #PRODUCTO
    path ('productos/', views.lista_productos, name= 'lista_productos'),
    path ('productos/<int:pepito>/', views.dame_producto, name="dame_producto"),
    path ('productos/<int:juanito>/editar', views.editar_producto, name="editar_producto"),
    path ('producto/<int:producto_id>', views.producto_eliminar, name="producto_eliminar"),
    path ('formulario/', views.crear_productos, name= 'crear_productos'),
    #TIENDA
    path ('tiendas/', views.lista_tiendas, name= 'lista_tiendas'),
    path ('tiendas/<int:pepito1>/', views.dame_tienda, name="dame_tienda"),
    path ('tiendas/<int:juanito1>/editar', views.editar_tienda, name="editar_tienda"),
    path ('tienda/<int:tienda_id>', views.tienda_eliminar, name="tienda_eliminar"),
    path ('formulario1/', views.crear_tiendas, name= 'crear_tiendas'),
    #CLIENTE
    path ('detalle/cliente/<int:id_cliente>', views.detalle_cliente,name= 'detalle_cliente'),
    #CUENTA BANCARIA
    path('crear/cuenta/', views.crear_cuenta, name='crear_cuenta'),
    path ('ver/cuenta/<int:id_cliente>', views.ver_cuenta, name = 'ver_cuenta'),
    path('eliminar/<int:id_cuenta>/cuenta/', views.eliminar_cuenta, name='eliminar_cuenta'), 
    path('editar/<int:id_cuenta>/cuenta', views.cuenta_editar, name='cuenta_editar'),
    #VENDEDOR
    path('detalles/vendedor/<int:id_vendedor>', views.detalle_vendedor, name='detalle_vendedor'), 
    path('ver/datos/<int:id_vendedor>', views.ver_datos, name='ver_datos'), 
    path('crear/datos/', views.crear_datos, name='crear_datos'), 
    path('eliminar/<int:id_vendedor>/datos/', views.eliminar_datos, name='eliminar_datos'), 
    path('editar/<int:id_vendedor>/datos', views.datos_editar, name='datos_editar'),
]
