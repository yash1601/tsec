from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, AccountForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def index(request):
    return render(request,'index.html')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('jobs')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def register(request):
    form = CreateUserForm()
    form2 = AccountForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form2 = AccountForm(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save()

            account = form2.save(commit=False)
            account.user = user

            account.save()
            messages.success(request, 'Registered successfully')
            return redirect('login')

    context = {'form': form,
               'form2': form2,
               }

    return render(request, 'register.html', context)