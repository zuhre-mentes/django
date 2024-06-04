import requests
from bs4 import BeautifulSoup
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import City
from django.http import HttpResponse
from django.contrib.auth.models import User



def home(request):
    return render(request, "index.html")

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/second/')

    return render(request, 'login.html')

def registration_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Kullanıcı adı olarak email'i kullanabilirsiniz
        username = email.split('@')[0]

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/registration/')

        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )

        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")
        return redirect('/registration/')

    return render(request, 'registration.html')
    
def second_page(request):
    cities = City.objects.all()
    return render(request, 'second.html', {'cities': cities})

def second_view(request):
    cities = City.objects.all()
    return render(request, 'second.html', {'cities': cities})


def city_detail(request, city_name):
    template_name = f'{city_name.lower()}.html'
    try:
        return render(request, template_name)
    except TemplateDoesNotExist:
        raise Http404('<h1>City not found</h1>')
