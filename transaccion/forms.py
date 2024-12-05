from django.forms import ModelForm
from .models import Transaccion

class TransaccionForm(ModelForm):
    class Meta:
        model = Transaccion
        fields = ['perfil', 'monto', 'tipo_transaccion', 'categoria', 'descripcion', 'fecha_transaccion']