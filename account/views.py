from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Perfil


from .forms import EditPerfilForm, EditUserForm

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('perfil')
        else:
            return redirect('login')
    else:
        if request.user.is_authenticated:
            
            return render(request, 'login/login.html')
        else:
            
            return render(request, 'login/login.html')
        
    
def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        user = User.objects.create_user(username, email, password)
        perfil = Perfil.objects.create(user=user.id)
        if user:
            login(request, user)
            return render(request, 'login/login.html', {'message': 'Usuario creado correctamente'})
        else:
            return render(request, 'login/register.html', {'error': 'No se pudo crear el usuario'})
    else:
        return render(request, 'login/register.html')


    

############### Account  ####################
@login_required
def perfil(request, id):
    user = request.user
    fuser= User.objects.filter(username=user.username).values()
    perfil = get_object_or_404(Perfil, user=user.id)
    perfil2 = Perfil.objects.filter(user=user.id).values()
    logo = get_logo(request)

    print(logo)
    return render(request, 'account/perfil.html', {
        'user': user,
        'fuser': fuser,
        'perfil': perfil,
        'logo': logo,
        })

def editar_perfil(request, id):
    if request.method == 'POST':
        user = request.user
        perfil = get_object_or_404(Perfil, user=user.id)
        form = EditPerfilForm(request.POST, request.FILES)
        logo = get_logo(request)
        if form.is_valid():
            perfil.user = user
            perfil.profesion = form.cleaned_data['profesion']
            perfil.puesto_actual = form.cleaned_data['puesto_actual']
            perfil.empresa = form.cleaned_data['empresa']
            perfil.telefono = form.cleaned_data['telefono']
            perfil.direccion = form.cleaned_data['direccion']
            perfil.ciudad = form.cleaned_data['ciudad']
            perfil.estado = form.cleaned_data['estado']
            perfil.pais = form.cleaned_data['pais']
            perfil.codigo_postal = form.cleaned_data['codigo_postal']
            perfil.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            perfil.genero = form.cleaned_data['genero']
            perfil.foto = form.cleaned_data['foto']
            perfil.curriculum = form.cleaned_data['curriculum']
            perfil.save()
            

            return render(request, 'account/perfil.html', {
                'perfil': perfil,
                'message': 'Perfil actualizado correctamente',
                'logo': get_logo(request),
                'form': form,
                })
        else:
            return render(request, 'account/editar_perfil.html', {
                'form': form,
                'perfil': perfil,
                'logo': logo,
                'error': perfil.errors,
                })
    else:
        user = request.user
        perfil = get_object_or_404(Perfil, user=user.id)
        form = EditPerfilForm(instance=perfil)
        logo = get_logo(request)
        return render(request, 'account/editar_perfil.html', {
            'form': form,
            'perfil': perfil,
            'logo': logo,
            })


