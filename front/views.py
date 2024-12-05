from django.shortcuts import render, redirect
from account.models import Perfil
from django.contrib.auth import authenticate
# Create your views here.

def home(request):
    user = request.user
    if user.is_authenticated:
        perfil = Perfil.objects.get(user=request.user)
        return render(request, 'pages/index.html',{
                    'perfil': perfil
                })
    else:
            return redirect('login')
        
    
    perfil = Perfil.objects.get(user=request.user)
    return render(request, 'pages/index.html',{
                    'perfil': perfil
                })