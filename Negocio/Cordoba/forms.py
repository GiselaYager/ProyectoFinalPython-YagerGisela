from django import forms

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