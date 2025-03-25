from django.shortcuts import render
from .models import *
from datetime import datetime
from .forms import *

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
    formulario = RegistroForm() #Mismo nombre que en forms.py
    return render (request, 'registration/signup.html', {'formulario': formulario} )