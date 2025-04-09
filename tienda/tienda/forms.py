from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.forms import ModelForm


class RegistroForm(UserCreationForm): #Mismo nombre que en views.py
    roles = (
        (Usuario.CLIENTE, 'cliente'),
        (Usuario.VENDEDOR, 'vendedor'),
    )
    
    rol = forms.ChoiceField(choices=roles)
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'rol')
        
class TiendaModelForm(ModelForm):
    class Meta:
        model = Tienda
        fields = ['nombre','direccion','telefono']
        labels = {
            "nombre": ("Nombre de la Tienda"),
            "direccion": ("Direccion de la tienda"),
            "telefono": ("Numero de Telefono")
        }
        
        
class ProductoModelForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','precio','tipoFruta']
        labels = {
            "nombre": ("Nombre de la Fruta"),
            "precio": ("Precio por Kilo"),
            "tipoFruta": ("Tipo de Fruta")
        }
        help_texts = {
            "nombre": ("200 caracteres maximo."),
            "precio": ("Se aceptan numeros decimales."),
            "tipoFruta": ("Acidas, Semiacidas, Neutras y Dulces.")
        }
        widgets = {
            
        }
        
    def clean(self):
        
        super().clean()
        
        nombre = self.cleaned_data.get('nombre')
        
        if len(nombre)< 5:
            self.add_error('nombre', 'Tiene que tener minimo 5 caracteres.')
            
        return self.cleaned_data