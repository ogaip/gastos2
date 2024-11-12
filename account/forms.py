from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Perfil
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        
class EditPerfilForm(ModelForm):
    class Meta:
        model = Perfil
        fields = [
            'user',
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
            'user': 'Usuario',
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
        
        
        
        