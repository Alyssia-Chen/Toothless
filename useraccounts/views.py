from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('classavails:index')
    else:
        form = UserCreationForm()
    return render(request, 'useraccounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in user
            user = form.get_user()
            login(request, user)
            return redirect('classavails:index')
    else:
        form = AuthenticationForm()
    return render(request, 'useraccounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('classavails:index') #Chage this redirect to landing page