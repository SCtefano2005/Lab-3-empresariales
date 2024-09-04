from django import forms
from .models import *


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [ 'name', 'lastname', 'email', 'dni', 'telefono', 'flat_number']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'lastname': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'telefono' : forms.TextInput(attrs={'Placeholder': 'Ingrese su numero de telefono'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese el DNI'}),
            'flat_number' : forms.TextInput(attrs={'placeholder': 'Ingrese el numero de departamento'}),
        }

class CarroForm(forms.ModelForm):
    
    tipo = forms.ModelChoiceField(
        queryset=Tipo_V.objects.all(),  # Obtiene todos los tipos de vehículos que guarde con el seeder
        required=True,
        widget=forms.Select(attrs={'placeholder': 'Seleccione el tipo de vehículo'}),
        empty_label="Seleccione un tipo"
    )
        
    dni = forms.CharField(max_length=8, required=True, widget=forms.TextInput(attrs={'placeholder':'Ingrese el DNI del propietario que se registro en el sistema'}))
    
    class Meta:
        model = Carro
        fields = ['placa', 'tipo', 'marca', 'modelo', 'color', 'dni'] 
        widgets = {
            'placa': forms.TextInput(attrs={'placeholder': 'Ingrese la placa'}),
            'marca': forms.TextInput(attrs={'placeholder': 'Ingrese la marca del vehículo'}),
            'modelo': forms.TextInput(attrs={'placeholder': 'Ingrese el modelo del vehículo'}),
            'color': forms.TextInput(attrs={'placeholder': 'Ingrese el color del vehículo'}),
        }
        
class CarroForm_editar(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['placa', 'tipo', 'marca', 'modelo', 'color', 'usuario']  

    placa = forms.CharField(
        label='Placa',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la placa', 'required': 'required'})
    )
    tipo = forms.ModelChoiceField(
        queryset=Tipo_V.objects.all(),
        label='Tipo',
        widget=forms.Select(attrs={'required': 'required'})
    )
    marca = forms.CharField(
        label='Marca',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese la marca del vehículo', 'required': 'required'})
    )
    modelo = forms.CharField(
        label='Modelo',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el modelo del vehículo', 'required': 'required'})
    )
    color = forms.CharField(
        label='Color',
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese el color del vehículo', 'required': 'required'})
    )
    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        label='Propietario (DNI)',
        widget=forms.Select(attrs={'required': 'required'})
    )
    
