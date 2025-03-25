from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class RegistroForm(UserCreationForm): #Mismo nombre que en views.py
    roles = (
        (Usuario.CLIENTE, 'cliente'),
        (Usuario.VENDEDOR, 'vendedor'),
    )
    
    rol = forms.ChoiceField(choices=roles)
    
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password', 'password2', 'rol')