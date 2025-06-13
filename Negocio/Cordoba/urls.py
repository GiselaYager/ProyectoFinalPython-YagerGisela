from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path ('bienvenida/', views.bienvenida, name= 'bienvenida'),
    
    path("clientes/",  views.ClienteList.as_view(), name="clientes"),
    path("clienteCreate/",  views.ClienteCreate.as_view(), name="clienteCreate"),
    path("clienteUpdate/<int:pk>/",  views.ClienteUpdate.as_view(), name="clienteUpdate"),
    path("clienteDelete/<int:pk>/", views.ClienteDelete.as_view(), name="clienteDelete"),
    
     
    path("vendedores/",  views.VendedorList.as_view(), name="vendedores"),
    path("vendedorCreate/",  views.VendedorCreate.as_view(), name="vendedorCreate"),
    path("vendedorUpdate/<int:pk>/",  views.VendedorUpdate.as_view(), name="vendedorUpdate"),
    path("vendedorDelete/<int:pk>/", views.VendedorDelete.as_view(), name="vendedorDelete"),
    
    
     
    path("unidades/",  views.UnidadList.as_view(), name="unidades"),
    path("unidadCreate/",  views.UnidadCreate.as_view(), name="unidadCreate"),
    path("unidadUpdate/<int:pk>/", views.UnidadUpdate.as_view(), name="unidadUpdate"),
    path("unidadDelete/<int:pk>/", views.UnidadDelete.as_view(), name="unidadDelete"),
    


    path('registro/', views.register, name="registro"),
    path('login/', views.loginRequest, name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('perfil/', views.editarPerfil, name='perfil'),
    path('agregar_avatar/', views.agregarAvatar, name="agregar_avatar"),
    
    path('about/', views.about, name='about'),
    path('buscarUnidad/', views.buscarUnidad, name="buscarUnidad"),
    
    path('', include('django.contrib.auth.urls'))
]
