from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('trabajos')

    else:    

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password') 

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('trabajos')

            else:
                messages.info(request, 'Email o contraseña incorrecta')
            


        context = {}
        return render(request, 'login/login.html', context)    


def logout_view(request):
    logout(request)
    return redirect('login')          
