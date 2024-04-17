from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import CreateUserForm,LoginForm
from . import forms
from django .contrib import auth
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.


def Homepage(request):
    return render(request, 'homepage.html')

class Register(View):
    def get(self, request):
        form = forms.CreateUserForm()  # Access the CreateUserForm class
        context = {'form': form}
        return render(request, 'register.html', context)
    
    
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_login')
        context = {
        'form' : form  
         }
        return render(request, 'register.html', context)
        
    
    




class MyLogin(View):
    def get(self, request):
        form = LoginForm()  # Create an empty login form
        context = {
            'loginform': form
        }
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)  # Create a login form with submitted data')
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log the user in
                return redirect('dashboard')  # Redirect to the dashboard URL
        context = {
            'loginform': form
        }
        return render(request, 'login.html', context)




def dashbord(request):
    return render(request, 'dashbord.html')