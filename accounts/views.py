from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("LOGIN ERROR, TRY AGAIN"))
            return redirect('home')
    else:
        return render(request, 'base.html')

def tournament(request):
    return render(request, 'tournament.html')
