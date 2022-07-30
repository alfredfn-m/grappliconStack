from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .theChoices import WEIGHT_CHOICES, AGE_CHOICES, RANK_CHOICES

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, 
            email=email, 
            password=password)
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
                sex = request.POST['sex']
                birthday = request.POST['birthday']
                rank = request.POST['rank']
                password = form.cleaned_data['password1']
                user = authenticate(request, 
                    email=email,
                    first_name=first_name,
                    last_name=last_name, 
                    password=password,
                    sex=sex,
                    birthday=birthday,
                    rank=rank,
                    )
                login(request, user)
                messages.success(request, ('REGRISTRATION SUCCESSFUL'))
                return redirect('home')
        else:
            form = CustomUserCreationForm()

        return render(request, 'register_user.html', {
            'form':form,
            })

def about(request):
    return render(request, 'about.html')

def tournament(request):
    return render(request, 'tournament.html')

def competitor(request):
    return render(request, 'competitor.html')

def history(request):
    if request.user.is_authenticated:
        return render(request, 'history.html')
    else:
        return redirect('home')

def account(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user_profile = CustomUser.objects.get(id=request.user.id)
            userRank = user_profile.rank
            form = CustomUserChangeForm(request.POST, instance=user_profile)
            if form.is_valid():
                rank = request.POST['rank']
                if checkRank(rank, userRank):
                    pass
                else:
                    pass
                form.save()
                messages.success(request, ('Update Completed'))
            else:
                messages.success(request, ('Update Failed'))
            return redirect('account')
        else:
            form = CustomUserChangeForm()

        return render(request, 'account.html', {
            'form':form,
        })
    else:
        return redirect('home')

def checkRank(rank, userRank):
    pass
