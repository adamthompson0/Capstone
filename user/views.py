from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import auth

# Create your views here.
def signup_view(request):
    if request.method == "GET":
        context = {
            'form': UserCreationForm()
        }
        return render(request, 'user/signup.html', context)
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('home')
        else:
            context = {
                'form': form
            }
            return render(request, 'user/signup.html', context)
        
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context)

def logout_view(request):
    auth.logout(request)
    return redirect('login')


