from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import Q


from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . models import *
from . forms import *


import datetime, random
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# _________________ saludo/bienvenida ________________

def bienvenida(request):
    hoy= datetime.datetime.now()
    contexto={"fecha": hoy}
    return render (request, "Cordoba/bienvenida.html", contexto)


# ____________________ CBV CRUD _______________________

class ClienteList(LoginRequiredMixin, ListView):
    model = Cliente

class ClienteCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Cliente
    fields = ["nombre", "apellido", "email"]    
    success_url = reverse_lazy("clientes")
    
    def test_func(self):
        return self.request.user.is_superuser

class ClienteUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cliente
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("clientes")
    
    def test_func(self):
        return self.request.user.is_superuser

class ClienteDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cliente
    success_url = reverse_lazy("clientes")
     
    def test_func(self):
        return self.request.user.is_superuser       
    

class VendedorList(LoginRequiredMixin, ListView):
    model = Vendedor

class VendedorCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Vendedor
    fields = ["nombre", "apellido", "email"]    
    success_url = reverse_lazy("vendedores")
    
    def test_func(self):
        return self.request.user.is_superuser

class VendedorUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vendedor
    fields = ["nombre", "apellido", "email"]
    success_url = reverse_lazy("vendedores")
    
    def test_func(self):
        return self.request.user.is_superuser
    

class VendedorDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vendedor
    success_url = reverse_lazy("vendedores")
    
    def test_func(self):
        return self.request.user.is_superuser       
    

class UnidadList(LoginRequiredMixin, ListView):
    model = Unidad

class UnidadCreate(LoginRequiredMixin,UserPassesTestMixin, CreateView):
    model = Unidad
    fields = ["nombre", "marca", "año_de_fabricacion", "color"]    
    success_url = reverse_lazy("unidades")
    
    def test_func(self):
        return self.request.user.is_superuser
    
class UnidadUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Unidad
    fields = ["nombre", "marca", "año_de_fabricacion", "color"]
    success_url = reverse_lazy("unidades")
    
    def test_func(self):
        return self.request.user.is_superuser

class UnidadDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Unidad
    success_url = reverse_lazy("unidades")
    
    def test_func(self):
        return self.request.user.is_superuser   
    


# _______________ Registracion / Login / Logout __________________

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('bienvenida'))
    else:
        miForm = RegistroForm()

    return render(request, "Cordoba/registro.html", {"form": miForm})   


def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)     
            #_______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/Media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________     
                  
            return render(request, "Cordoba/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "Cordoba/login.html", {"form": miForm})



# ____________________  Edit Perfil de usuario ________________

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("bienvenida"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "Cordoba/editarPerfil.html", {"form": miForm})

# __________________________ Avatar ___________________________

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen a bienvenida
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("bienvenida"))
    else:
        miForm = AvatarForm()
    return render(request, "Cordoba/agregarAvatar.html", {"form": miForm})  

  
# __________________________ Acerca de mi ___________________________

def about(request):
        context = {
        }
        return render(request,"Cordoba/acercademi.html",context)
    
    
# ___________________ Búsqueda de unidades disponibles_______________

def buscarUnidad(request):
    form = BuscarProductoForm(request.GET or None)
    unidades = Unidad.objects.all()

    if form.is_valid():
        patron = form.cleaned_data['patron']
        if patron:
            unidades = unidades.filter(
                Q(nombre__icontains=patron) |
                Q(marca__icontains=patron) |
                Q(color__icontains=patron) |
                Q(año_de_fabricacion__icontains=patron)
            )

    return render(request, 'Cordoba/buscar_unidad.html', {'form': form, 'unidades': unidades})
