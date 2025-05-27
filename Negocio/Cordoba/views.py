from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from . forms import *
import datetime, random
# Create your views here.

def bienvenida(request):
    hoy= datetime.datetime.now()
    contexto={"fecha": hoy, "nombre": "Gisela", "apellido": "Yager"}
    return render (request, "Cordoba/bienvenida.html", contexto)

def nuevo_cliente(request):
    nombre= random.choices(["Juan", "Camila", "Emilia", "Santiago"], k=1)[0]
    apellido= random.choices(["Yager", "Rodriguez", "Martinez","Perez"], k=1)[0]
    cliente= Cliente(nombre=nombre, apellido=apellido)
    cliente.save()
    return render (request, "Cordoba/nuevo_cliente.html", {"cliente": nombre, "apellido": apellido })

def clientes(request):
    clientes = Cliente.objects.all()
    return render(request, "Cordoba/clientes.html", {"clientes": clientes})

def vendedores(request):
    vendedores = Vendedor.objects.all()
    return render(request, "Cordoba/vendedores.html", {"vendedores": vendedores})

def unidades(request):
    unidades= Unidad.objects.all()
    return render(request,"Cordoba/unidades.html", {"unidades": unidades})
    

def clienteForm(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            email = form.cleaned_data["email"]
            cliente = Cliente(nombre=nombre, apellido=apellido, email=email)
            cliente.save()
            clientes = Cliente.objects.all()
            return render(request, "Cordoba/clientes.html", {"clientes": clientes})
    else:
        form = ClienteForm()
    return render(request, "Cordoba/cliente_form.html", {"form": form})


def vendedorForm(request):
    if request.method == "POST":
        form = VendedorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            vendedor = Vendedor(nombre=nombre, apellido=apellido)
            vendedor.save()
            vendedores = Vendedor.objects.all()
            return render(request, "Cordoba/vendedores.html", {"vendedores": vendedores})
    else:
        form =VendedorForm()
    return render(request, "Cordoba/vendedor_form.html", {"form": form})


def unidadForm(request):
    if request.method == "POST":
        form = UnidadForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            marca = form.cleaned_data["marca"]
            año_de_fabricacion = form.cleaned_data["año_de_fabricacion"]
            color= form.cleaned_data["color"]
            unidad = Unidad(nombre=nombre, marca=marca, año_de_fabricacion=año_de_fabricacion, color=color)
            unidad.save()
            unidades = Unidad.objects.all()
            return render(request, "Cordoba/unidades.html", {"unidades": unidades})
    else:
        form = UnidadForm()
    return render(request, "Cordoba/unidad_form.html", {"form": form})



def buscar(request):
    return render(request, "Cordoba/buscar.html")

def buscarUnidad(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        unidades = Unidad.objects.filter(nombre__icontains=patron)
        contexto = {"unidades": unidades }
        return render(request, "Cordoba/unidades.html", contexto)
    return HttpResponse("No se ingresaron patrones de busqueda")
