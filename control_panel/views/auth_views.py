from django.shortcuts import render

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def password(request):
    return render(request, 'pages/password.html')