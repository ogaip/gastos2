from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Perfil

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
class EditPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'profesion',
            'puesto_actual',
            'empresa',
            'telefono',
            'direccion',
            'ciudad',
            'estado',
            'pais',
            'codigo_postal',
            'fecha_nacimiento',
            'genero',
            'foto',
            'curriculum',
        ]
        labels = {
            'profesion': 'Profesion',
            'puesto_actual': 'Puesto Actual',
            'empresa': 'Empresa',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'pais': 'Pais',
            'codigo_postal': 'Codigo Postal',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'genero': 'Genero',
            'foto': 'Foto',
            'curriculum': 'Curriculum',
        }
        
        widgets = {
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'puesto_actual': forms.TextInput(attrs={'class': 'form-control'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'required': 'false'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'pais': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo_postal': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.Select(choices=Perfil.GENERO_CHOICES, attrs={'class': 'form-control'}),
            'foto': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'accept': 'image/*'}),
            'curriculum': forms.FileInput(attrs={'class': 'form-control', 'type': 'file', 'accept': ['.pdf', '.doc', '.docx']}),
            
                }