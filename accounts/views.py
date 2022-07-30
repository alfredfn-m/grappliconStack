from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm

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
            messages.success(request, ('LOGIN ERROR, TRY AGAIN'))
            return redirect('home')
    else:
        return render(request, 'base.html')

def logout_user(request):
    logout(request)
    messages.success(request, ('Logged Out'))
    return redirect('home')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                email = form.cleaned_data['email']
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                password = form.cleaned_data['password1']
                user = authenticate(email=email, first_name=first_name, last_name=last_name, password=password)
                login(request, user)
                messages.success(request, ('REGRISTRATION SUCCESSFUL'))
                return redirect('home')
        else:
            form = CustomUserCreationForm()

        return render(request, 'register_user.html', {
            'form':form,
            })


def tournament(request):
    return render(request, 'tournament.html')
