from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse


def register(request):
    error = None

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password != password2:
            error = 'As senhas não coincidem.'
        elif User.objects.filter(email=email).exists():
            error = 'Este email já está cadastrado.'
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect(reverse('register_success')) 

    return render(request, 'register.html', {'error': error})



def login_user(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')  
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)  


        if user is not None:
            login(request, user)
            return redirect('mainpage')  
        else:
            return render(request, 'login.html', {'error': 'Credenciais de login inválidas. Por favor, tente novamente.'})



def register_success(request):
    return render(request, 'register_success.html')

def logout_user(request):
    logout(request)
    return redirect('mainpage')

# Create your views here.
