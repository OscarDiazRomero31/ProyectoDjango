from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from django.contrib import messages

# Create your views here.
def index(request):
    
    if(not "fecha_inicio" in request.session):
        request.session["fecha_inicio"] = datetime.now().strftime('%d/%m/%Y %H:%M')
        
    return render(request, 'index.html', {})


@permission_required('tienda.view_cliente')
def lista_clientes(request):
    clientes = Cliente.objects.all()
    #clientes = None //nos mostraria en el template el mensaje de no hay clientes.
    return render(request,'cliente/lista_clientes.html', {'clientes_mostrar': clientes})


@permission_required('tienda.view_vendedor')
def lista_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request,'vendedor/lista_vendedores.html',{'vendedores_mostrar': vendedores})


@permission_required('tienda.view_productos')
def lista_productos(request):
    productos = Producto.objects.all()
    return render(request,'producto/lista_productos.html',{'productos_mostrar': productos})


@permission_required('tienda.add_productos')
def crear_productos(request):
    if request.method == "POST":
        formulario = ProductoModelForm(request.POST)
        if formulario.is_valid():
            print("Es valido")
            formulario.save()
            messages.success(request, 'Se ha creado la fruta')
            return redirect('lista_productos')
    else:
        formulario = ProductoModelForm()
    return render(request,'formularioProducto/crear_productos.html',{'crear_productos': formulario})


def lista_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request,'tienda/lista_tiendas.html',{'tiendas_mostrar': tiendas})


def crear_tiendas(request):
    if request.method == 'POST':
        formulario = TiendaModelForm(request.POST)
        if formulario.is_valid():
            print("Es valido")
            formulario.save()
            return redirect('lista_tiendas')
    else:
        formulario = TiendaModelForm()
    return render(request, 'formularioTienda/crear_tiendas.html',{'crear_tiendas': formulario})
            
        
def dame_producto(request,pepito):
    fruta = Producto.objects.get(id=pepito)
    return render(request, 'fruta_detalle/fruta_detalle.html',{'producto': fruta})

def dame_tienda(request,pepito1):
    tienda = Tienda.objects.get(id=pepito1)
    return render(request, 'tienda_detalle/tienda_detalle.html',{'tienda': tienda})


def editar_producto(request,juanito):
    producto = Producto.objects.get(id=juanito)
    
    if request.method == "POST":
        formulario = ProductoModelForm(request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se ha modificado la fruta')
            return redirect('dame_producto', pepito=producto.id)
    else:
        formulario = ProductoModelForm(instance=producto)
        
    return render(request, 'producto/editar_productos.html',{'editar_producto': formulario , "producto_editar" : producto})

def editar_tienda(request,juanito1):
    tienda = Tienda.objects.get(id=juanito1)
    
    if request.method == "POST":
        formulario =TiendaModelForm(request.POST, instance=tienda)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se ha modificado la tienda')
            return redirect('dame_tienda', pepito1=tienda.id)
    else:
        formulario = TiendaModelForm(instance=tienda)
            
    return render(request, 'tienda/editar_tiendas.html', {'editar_tienda': formulario, "tienda_editar": tienda})


def registrar_usuario(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            rol = int(formulario.cleaned_data.get('rol'))
            if(rol == Usuario.CLIENTE):
                grupo = Group.objects.get(name= 'clientes')
                grupo.user_set.add(user)
                cliente = Cliente.objects.create(usuario = user)
                cliente.save()
            elif(rol == Usuario.VENDEDOR):
                grupo = Group.objects.get(name='vendedores') 
                grupo.user_set.add(user)
                vendedor = Vendedor.objects.create(usuario = user)
                vendedor.save()
            
            login(request, user)
            return redirect('inicio')
    else:
        formulario = RegistroForm()
    return render(request, 'registration/signup.html', {'formulario': formulario})

def producto_eliminar(request,producto_id):
    producto = Producto.objects.get(id=producto_id)
    try:
        producto.delete()
        messages.success(request, "Se ha eliminado el producto")
    except Exception as error:
        print (error)
    return redirect('lista_productos')

def perfil(request,cliente_id):
    perfil = Cliente.objects.all()
    return render(request,'perfil/ver_cliente.html',{'ver_cliente': perfil, 'cliente_id': cliente_id})

def crear_cuentaBancaria(request):
    if request.method == 'POST':
        formulario = CuentaBancariaModelForm(request.POST)
        if formulario.is_valid():
            print("Es valido")
            formulario.save()
            return redirect('perfil')
    else:
        formulario = CuentaBancariaModelForm()
    return render(request, 'formularioCuentaBancaria/crear_cuentaBancaria.html',{'crear_cuentaBancaria': formulario})

