from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from .forms import *
from django.contrib.auth import login
from django.contrib.auth.models import Group

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
            user = formulario.save()
            rol = int(formulario.cleaned_data.get('rol'))
            if(rol == Usuario.CLIENTE):
                grupo = Group.objects.get(name= 'clientes')
                grupo.user_set.add(user)
                cliente = Cliente.objects.create(usuario = user)
                cliente.save()
            return redirect('inicio')
    else:
        formulario = RegistroForm()
    return render(request, 'registration/signup.html', {'formulario': formulario})