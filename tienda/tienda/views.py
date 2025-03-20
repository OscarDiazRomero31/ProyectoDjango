from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def lista_clientes(request):
    clientes = Cliente.objects.all()
    #clientes = None //nos mostraria en el template el mensaje de no hay clientes.
    return render(request,'cliente/lista_clientes.html', {'clientes_mostrar': clientes})

