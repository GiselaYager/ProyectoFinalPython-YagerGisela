from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"  

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}" 
    

class Unidad(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    año_de_fabricacion = models.IntegerField()
    color = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre}, {self.marca}" 
    
    
class Avatar(models.Model):   
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 
