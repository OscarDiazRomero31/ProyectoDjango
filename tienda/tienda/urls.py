from django.urls import path, include
from . import views

urlpatterns = [
    path ('',views.index, name = 'inicio'),
    path ('clientes/', views.lista_clientes, name= 'lista_clientes'),
    path ('registrar', views.registrar_usuario, name='registrar_usuario'),
    path ('accounts/', include('django.contrib.auth.urls')),
    path ('vendedores/', views.lista_vendedores, name= 'lista_vendedores'),
]
