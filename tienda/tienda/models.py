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
    
    def __str__(self):
        return self.nombre
    
class Tienda (models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    telefono = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
    vendedor = models.ForeignKey(Vendedor, on_delete=
                                 models.CASCADE, default=None, null=True)
    
    producto = models.ManyToManyField(Producto,
                                      through='Inventario')
                                      #related_name='producto'
    
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
    
    
class DatosVendedor(models.Model):
  direccion = models.CharField(max_length=50)
  facturacion = models.CharField(max_length=50)

  vendedor = models.OneToOneField(Vendedor, on_delete=models.CASCADE)      
    
class Inventario(models.Model):
    tienda =models.ForeignKey(Tienda, on_delete=models.CASCADE)
    producto =models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad =models.IntegerField()