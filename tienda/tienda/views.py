from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.http import Http404

# Create your views here.
def index(request):
    
    if(not "fecha_inicio" in request.session):
        request.session["fecha_inicio"] = datetime.now().strftime('%d/%m/%Y %H:%M')   
    return render(request, 'index.html', {})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    #clientes = None //nos mostraria en el template el mensaje de no hay clientes.
    return render(request,'cliente/lista_clientes.html', {'clientes_mostrar': clientes})

def lista_vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request,'vendedor/lista_vendedores.html',{'vendedores_mostrar': vendedores})

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request,'producto/lista_productos.html',{'productos_mostrar': productos})

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
            tienda = Tienda.objects.create(
                nombre = formulario.cleaned_data.get("nombre"),
                direccion = formulario.cleaned_data.get("direccion"),
                telefono = formulario.cleaned_data.get("telefono"),
                vendedor = request.user.vendedor
            )
            tienda.save()
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

def tienda_eliminar(request,tienda_id):
    tienda = Tienda.objects.get(id=tienda_id)
    try:
        tienda.delete()
        messages.success(request, "Se ha eliminado la tienda")
    except Exception as error:
        print (error)
    return redirect('lista_tiendas')

def detalle_cliente(request, id_cliente):
    if request.user.cliente.id == id_cliente:
        cliente = Cliente.objects.get(id = id_cliente)
        return render (request, 'cliente/detalles_cliente.html', {'cliente': cliente} )
    else:
        raise Http404()

def crear_cuenta(request):
    if request.method == 'POST':
        formulario = CuentaBancariaModelForm(request.POST)
        if formulario.is_valid():
            cuenta = CuentaBancaria.objects.create(
                IBAN = formulario.cleaned_data.get("IBAN"),
                banco = formulario.cleaned_data.get("banco"),
                moneda = formulario.cleaned_data.get("moneda"),
                cliente = request.user.cliente,  
            )
            cuenta.save()
            messages.success(request, 'Se ha creado su cuenta')  
            return redirect ("detalle_cliente", id_cliente=request.user.cliente.id)
    else:
        formulario = CuentaBancariaModelForm()

    return render (request, 'cliente/crear_cuenta.html', {'formulario': formulario})

def ver_cuenta(request, id_cliente):
    cuenta = CuentaBancaria.objects.filter(cliente_id=id_cliente).first()
    
    return render (request, 'cliente/cuenta.html', {'cuenta' : cuenta} )

def eliminar_cuenta(request, id_cuenta):
    cuenta = CuentaBancaria.objects.get(id=id_cuenta)

    try:
        cuenta.delete()  
        messages.success(request, "Se ha eliminado la cuenta bancaria correctamente.")
    except Exception as error:
        print(error)

    return redirect('ver_cuenta', id_cliente=cuenta.cliente.id)

def cuenta_editar(request, id_cuenta):
    cuenta = CuentaBancaria.objects.get(id = id_cuenta)
    
    if request.method == "POST": 
        formulario = CuentaBancariaModelForm(request.POST, instance=cuenta)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Se ha modificado perfectamente')            
        return redirect('ver_cuenta', id_cliente=cuenta.cliente.id) 
    else:
        formulario = CuentaBancariaModelForm(instance=cuenta)     
        
    return render (request, 'cliente/cuenta_editar.html', {'formulario' : formulario, 'cuenta' : cuenta })

def detalle_vendedor(request, id_vendedor):
    vendedor = Vendedor.objects.get(id = id_vendedor)
    
    return render (request, 'vendedor/detalle_vendedor.html', {'vendedor': vendedor} )

def ver_datos(request, id_vendedor):
    vendedor = DatosVendedor.objects.filter(vendedor_id=id_vendedor).first()
    
    return render (request, 'vendedor/datos_vendedor.html', {'vendedor' : vendedor} )

def crear_datos(request):
    if request.method == 'POST':
        formulario = DatosModelForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Se han Creado sus Datos')  
            return redirect ('detalle_vendedor', id_vendedor=request.user.vendedor.id)
    else:
        formulario = DatosModelForm()

    return render (request, 'vendedor/crear_datos.html', {'formulario': formulario})

def eliminar_datos (request, id_vendedor):
    vendedor = DatosVendedor.objects.get(id=id_vendedor)

    try:
        vendedor.delete()  
        messages.success(request, "Se han eliminado los datos correctamente.")
    except Exception as error:
        print(error)

    return redirect('ver_datos', id_vendedor=vendedor.vendedor.id) 

def datos_editar(request, id_vendedor):
    vendedor = DatosVendedor.objects.get(id = id_vendedor)
    
    if request.method == "POST": 
        formulario = DatosModelForm(request.POST, instance=vendedor)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, 'Se ha modificado perfectamente')            
        return redirect('ver_datos', id_vendedor=vendedor.vendedor.id) 
    else:
        formulario = DatosModelForm(instance=vendedor)     
        
    return render (request, 'vendedor/datos_editar.html', {'formulario' : formulario, 'vendedor' : vendedor })

def crear_inventario(request):
    if request.method == "POST":
        formulario = InventarioModelForm(request.POST, request=request)
        if formulario.is_valid():
            #print("Es valido")
            inventario = Inventario.objects.filter(tienda = formulario.cleaned_data.get('tienda'),
                                                   producto = formulario.cleaned_data.get('producto')).first()
            if (inventario is None):
                formulario.save()
            else:
                inventario.cantidad += formulario.cleaned_data.get("cantidad")
                formulario.save()
            messages.success(request, 'Se ha añadido a la tienda el producto')
            return redirect('lista_tiendas')
    else:
        formulario = InventarioModelForm(None,request=request)
    return render(request,'formularioInventario/crear_inventario.html',{'crear_inventario': formulario})

def lista_productosTienda(request, tienda_id):
    productos = Inventario.objects.filter(tienda_id=tienda_id)

    return render(request, 'inventario/lista_productos.html', {'productos': productos})

def mi_error_404(request,exception=None):
    return render(request, 'errores/404.html', None, None, 404)

def mi_error_500(request,exception=None):
    return render(request, 'errores/500.html', None, None, 500)