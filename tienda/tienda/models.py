from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    ADMINISTRADOR = 1
    CLIENTE = 2
    VENDEDOR = 3
    ROLES = (
        (ADMINISTRADOR, 'administrador'),
        (CLIENTE, 'cliente'),
        (VENDEDOR, 'vendedor'),
    )
    
    rol = models.PositiveSmallIntegerField(
        choices=ROLES,default=2
    )

class Cliente (models.Model):
    usuario = models.OneToOneField(Usuario,
                                   on_delete = models.CASCADE)

    def __str__(self):
        return self.usuario.username

class Vendedor (models.Model):
    usuario = models.OneToOneField(Usuario,
                                   on_delete = models.CASCADE)
    
    def __str__(self):
        return self.usuario.username
    
class Producto (models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    tipoFruta = models.CharField(max_length=100)
    
class Tienda (models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    
class CuentaBancaria (models.Model):
    MONEDAS = [
        {"EUR", "Euros"},
        {"DOL", "Dollar"},
        {"LIB", "Libras"}
    ]
    IBAN = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    monedas = models.CharField(
        max_length=50,
        choices=MONEDAS,
        default="EUR",
    )
    cliente = models.OneToOneField(Cliente,
                                   on_delete = models.CASCADE)
    
    
        
    
    