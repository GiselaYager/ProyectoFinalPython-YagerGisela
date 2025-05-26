from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.IntegerField()
    email = models.EmailField()  

    def __str__(self):
        return f"{self.apellido} {self.nombre}"   

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()  

    def __str__(self):
        return f"{self.apellido}, {self.nombre}"  

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    año_de_fabricacion = models.IntegerField()
    color = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.nombre}, {self.marca}"  

