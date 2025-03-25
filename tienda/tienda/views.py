from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .forms import *
from django.contrib.auth import login

# Create your views here.
def index(request):
    
    if(not "fecha_inicio" in request.session):
        request.session["fecha_inicio"] = datetime.now().strftime('%d/%m/%Y %H:%M')
        
    return render(request, 'index.html', {})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    #clientes = None //nos mostraria en el template el mensaje de no hay clientes.
    return render(request,'cliente/lista_clientes.html', {'clientes_mostrar': clientes})

def registrar_usuario(request):
    if request.method == 'POST':
        formulario = RegistroForm(request.POST)
        if formulario.is_valid():
            # Obtención de los datos del formulario
            user = formulario.save()
            rol = int(formulario.cleaned_data.get('rol'))

            # Crear usuario y asignar rol
            if rol == Usuario.CLIENTE:
                cliente = Cliente.objects.create(usuario=user)
                cliente.save()
            elif rol == Usuario.VENDEDOR:
                bibliotecario = Vendedor.objects.create(usuario=user)
                bibliotecario.save()

            # Iniciar sesión del usuario
            login(request, user)
            return redirect('index')
    else:
        formulario = RegistroForm()

    return render(request, 'registration/signup.html', {'formulario': formulario})