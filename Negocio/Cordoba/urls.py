from django.urls import path
from . import views

urlpatterns = [
    path ('bienvenida/', views.bienvenida, name= 'bienvenida'),
    path ('nuevo_cliente/', views.nuevo_cliente, name= 'nuevo_cliente'),
    
    path("clientes/",  views.clientes, name="clientes"),
    path("cliente_form/",  views.clienteForm, name="cliente_form"),

    path("vendedores/",  views.vendedores, name="profesores"),
    path("vendedor_form/",  views.vendedorForm, name="vendedor_form"),
    
    path("unidades/",  views.unidades, name="unidades"),
    path("unidad_form/",  views.unidadForm, name="unidad_form"),
    
    path('buscar/', views.buscar, name="buscar"),
    path('buscarUnidad/', views.buscarUnidad, name="buscarUnidad"),
]
