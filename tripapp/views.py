from django.shortcuts import render

def login_page(request):
    return render(request, 'login.html')


def registration_page(request):
    return render(request, 'registration.html')

