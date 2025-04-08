from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required

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
            return redirect('lista_productos')
    else:
        formulario = ProductoModelForm()
    return render(request,'formularioProducto/crear_productos.html',{'crear_productos': formulario})

def lista_tiendas(request):
    tiendas = Tienda.objects.all()
    return render(request,'tienda/lista_tiendas.html',{'tiendas_mostrar': tiendas})

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


