from django import forms
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm


class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre", required=True)
    apellido = forms.CharField(max_length=50, label= "Apellido", required=True)
    email= forms.EmailField(required=True)
    

class VendedorForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre del vendedor", required=True)
    apellido = forms.CharField(max_length=50, label="Apellido del vendedor", required=True)
    
    
class UnidadForm(forms.Form):
    nombre= forms.CharField(max_length=50, label="Nombre de la unidad", required=True)
    marca= forms.CharField(max_length=50, label="Marca", required=True)
    año_de_fabricacion= forms.IntegerField(label="Año de Fabricación", required=True)
    color = forms.CharField(max_length=50, label="Color")
    
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]   
        

class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #  Oculta el campo de contraseña (que hereda del UserChangeForm)
        if 'password' in self.fields:
            self.fields['password'].help_text = None
            self.fields['password'].widget = forms.HiddenInput()     
        
        
        
        
        
        
        
        
        

  
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)       
    
class BuscarProductoForm(forms.Form):
    patron = forms.CharField(label='Buscar producto', max_length=100, required=False)  
