from django.shortcuts import render
from .forms import TransaccionForm
# Create your views here.

def gastos(request):
    form = TransaccionForm()
    perfil = request.user.perfil
    
    return render(request, "transacciones/gastos.html", 
                  {"form": form, 
                   "perfil": perfil})
    
