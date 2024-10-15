from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from control_panel.forms import CustomUserUpdateForm, InsertNewUserForm
from sitesetup.context_processors import user_log_activity
from django.contrib.auth.models import User
from sitesetup.context_processors import get_client_ip


@login_required
def user_data(request):
    user_data = request.user
    form = CustomUserUpdateForm(instance=user_data)
    if request.method == 'POST':
        if 'password_change' in request.POST:
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')
            if new_password1 == new_password2:
                user_log_activity(
                    user_data,
                    'Alterou sua senha',
                    get_client_ip(request)
                    )
                return password_change(request, user_data, new_password1)
            else:
                user_log_activity(
                    user_data,
                    'Senha diferentes ao alterar',
                    get_client_ip(request)
                    )
                print(f'Senhas incomaptíveis: {new_password1} é diferente de {new_password2}')
                return redirect('control_panel:user_data')
        else:
            form = CustomUserUpdateForm(request.POST, instance=user_data)
            if form.is_valid():
                form.save()
                changed_values = [field for field in form.changed_data]
                user_log_activity(
                    user_data,
                    f'Dados de usuário: {changed_values}',
                    get_client_ip(request)
                    )
                print('Dados de usuário alterados com sucesso')
                return redirect('control_panel:user_data')
            else:
                user_log_activity(
                    user_data,
                    f'Erro nos dados de usuário',
                    get_client_ip(request)
                    )
                print(f'Erro ao salvar os dados de usuário: {form.errors}')
                return redirect('control_panel:user_data')

    context = {
        'form':form,
    }
    return render(request, 'pages/user_data.html', context)

def password_change(request, user_data, new_password):
    user_data.set_password(new_password)
    user_data.save()
    logout(request)
    return redirect('control_panel:login')


def users(request):
    user_data = request.user
    users = User.objects.all().order_by('first_name')
    if request.method == 'POST':
        form = InsertNewUserForm(request.POST)
        email_exists = request.POST.get('email')
        user_exists = request.POST.get('username')
        try:
            if User.objects.filter(email=email_exists).exists() or User.objects.filter(username=user_exists).exists():
                print(f'Email ou Nome de Usuário já registrado')
            else:
                if form.is_valid():
                    form.save()
                    user_log_activity(
                        user_data,
                        'Novo usuário registrado',
                        get_client_ip(request),
                    )
                    print('Novo usuário criado com sucesso')
                    return redirect('control_panel:users')
            
        except Exception as error:
            print(f'Erro ao criar usuário: {error}')
        
    form = InsertNewUserForm()

    context = {
        'data_table': users,
        'form': form,
    }

    return render(request, 'pages/users.html', context)

def edit_user(request, id):
    user_data = request.user
    user_obj = User.objects.get(id=id)
    users = User.objects.all().order_by('first_name')

    if request.method == 'POST':
        print(request.POST)
        form = InsertNewUserForm(request.POST, instance=user_obj)
        
        if form.is_valid():
            new_password1 = form.cleaned_data.get('password1')
            if new_password1:
                user_obj.set_password(new_password1)
                user_log_activity(
                    user_data,
                    f'Senha de usuário {user_obj} alterada',
                    get_client_ip(request),
                )
                print(f'Senha de usuário {user_obj} alterada')

            form.save()
            user_log_activity(
                user_data,
                'Usuário editado',
                get_client_ip(request),
            )
            print('Usuário editado com sucesso')
            return redirect('control_panel:users')
        else:
            print('Erro de validação de formulário de edição do usuário')
    else:
        form = InsertNewUserForm(instance=user_obj)

    context = {
        'data_table': users,
        'form': form,
    }

    return render(request, 'pages/users.html', context)

def delete_user(request, id):
    user_data = request.user
    user_obj = User.objects.get(id=id)
    try:
        user_obj.delete()
        user_log_activity(
            user_data,
            f'Usuário {user_obj} deletado',
            get_client_ip(request),
        )
        print(f'Usuário {user_obj} deletado')
    except Exception as error:
        print(f'Erro ao deletar {user_obj}: {error}')
    return redirect('control_panel:users')
    