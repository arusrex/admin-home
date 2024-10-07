from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import check_password
from django.core.mail import send_mail
from sitesetup.models import EmailBackend

def logar(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('control_panel:home')
            else:
                return render(request, 'pages/login.html')
    except Exception as error:
        print(f'Falha na autênticação: {error}')
        return redirect('control_panel:login')
    return render(request, 'pages/login.html')

@login_required
def deslogar(request):
    logout(request)
    return redirect('control_panel:login')

def register(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']

            if password1 != password2:
                print(f'Senhas incompatíveis: {password1} - {password2}')
                return redirect('control_panel:register')

            try:
                validate_password(password1)
            except ValidationError as e:
                print(f'Erro de validação da senha: {e}')
                return redirect('control_panel:register')
            
            if User.objects.filter(username=username).exists():
                return redirect('control_panel:register')
            if User.objects.filter(email=email).exists():
                return redirect('control_panel:register')
            
            new_user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password1,
                    first_name=first_name,
                    last_name=last_name
                    )
            
            return redirect('control_panel:login')
        
    except Exception as error:
        print(f'Erro ao registrar usuário: {error}')
        return redirect('control_panel:register')       
    return render(request, 'pages/register.html')

def enviar_email_password(request):
    try:
        email_backend = EmailBackend.objects.last()
        if not email_backend:
            print('Email de backend não configurado')
            return redirect('control_panel:site_setup')
        
        email_password = request.POST.get('email', None)
        if not email_password:
            print('E-mail não informado para envio')
            return redirect('control_panel:password')
        
        from_email = email_backend.default_from_email
        subject = 'Recuperação de senha'
        message = 'É necessário a alteração do seu-email, clique no link a seguir para realizar o procedimento'
        recipient_list = [email_password]

        send_mail(
            subject,
            message,
            from_email,
            recipient_list,
            fail_silently=False,
            connection=None,
        )

        print('Email evnviado com sucesso')
        return redirect('control_panel:password')
    except Exception as error:
        print(f'Erro ao enviar email de recuperação: {error}')

    return render(request, 'pages/password.html')