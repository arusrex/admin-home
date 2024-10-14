from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from sitesetup.models import EmailBackend
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from sitesetup.context_processors import user_log_activity
from django.utils.crypto import get_random_string


def logar(request):
    try:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                user_log_activity(
                    user,
                    'Login',
                    request.META.get('REMOTE_ADDR'),
                )
                print(f'{user.username} logado com sucesso')
                return redirect('control_panel:home')
            else:
                return render(request, 'pages/login.html')
    except Exception as error:
        print(f'Falha na autênticação: {error}')
        return redirect('control_panel:login')
    return render(request, 'pages/login.html')

@login_required
def deslogar(request):
    user_data = request.user
    logout(request)
    user_log_activity(
        user_data,
        'Logout',
        request.META.get('REMOTE_ADDR'),
    )
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
            
            user_log_activity(
                new_user,
                'Usuário registrado',
                request.META.get('REMOTE_ADDR'),
            )
            
            return redirect('control_panel:login')
        return render(request, 'pages/register.html')
        
    except Exception as error:
        print(f'Erro ao registrar usuário: {error}')
        return redirect('control_panel:register')
    finally:
        return render(request, 'pages/register.html')


def enviar_email_password(request):
    try:
        if request.method == 'POST':
            email_backend = EmailBackend.objects.last()

            if not email_backend:
                print('Email de backend não configurado')
                return redirect('control_panel:site_setup')
            
            email_password = request.POST.get('email_esquecido', None)
            if not email_password:
                print('E-mail não informado para envio')
                return redirect('control_panel:password')
            
            user_by_email = User.objects.get(email=email_password)
            if user_by_email:
                pass_random = get_random_string(length=8)
                user_by_email.is_active = True
                user_by_email.set_password(pass_random)
                user_by_email.save()
            else:
                print('Email não consta na base de dados')

            
            from_email = email_backend.default_from_email
            subject = 'Recuperação de senha'
            message_body = f'Olá {user_by_email.username}, sua nova senha provisória é: {pass_random}, é extremamente recomendável alterar a senha provisória o quanto antes.'
            recipient_list = [email_password]
            smtp_username = email_backend.email_host_user
            smtp_password = email_backend.email_host_password.strip()
            smtp_server = email_backend.email_host
            smtp_port = email_backend.email_port
            smtp_tls = email_backend.email_use_tls

            # Cria a mensagem MIME
            message = MIMEMultipart()
            message['From'] = from_email
            message['To'] = email_password
            message['Subject'] = subject
            message.attach(MIMEText(message_body, 'plain'))

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.ehlo()
                if smtp_tls:
                    server.starttls()
                    server.ehlo()
                server.login(smtp_username, smtp_password)
                server.sendmail(from_email, recipient_list, message.as_string())
                print('Email enviado com sucesso')

            return redirect('control_panel:login')
        return render(request, 'pages/password.html')
    except Exception as error:
        print(f'Erro ao enviar email de recuperação: {error}')
        return redirect('control_panel:password')
