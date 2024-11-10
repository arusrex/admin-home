from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from control_panel.forms import CustomUserUpdateForm, UserCreationForm, InsertNewUserForm, UpdateUserForm
from sitesetup.context_processors import user_log_activity
from django.contrib.auth.models import User
from sitesetup.context_processors import get_client_ip
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, SetPasswordForm

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
                messages.success(request, "Senha alterada !")
                return password_change(request, user_data, new_password1)
            else:
                user_log_activity(
                    user_data,
                    'Senha diferentes ao alterar',
                    get_client_ip(request)
                    )
                messages.error(request, "Senhas incomaptíveis !")
                print(f'Senhas incomaptíveis !')
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
                messages.success(request, "Dados de usuário alterados com sucesso")
                print('Dados de usuário alterados com sucesso')
                return redirect('control_panel:user_data')
            else:
                user_log_activity(
                    user_data,
                    f'Erro nos dados de usuário',
                    get_client_ip(request)
                    )
                messages.error(request, 'Erro ao salvar os dados de usuário')
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
    return user_form(request)

def edit_user(request, id):
    return user_form(request, id, action_none='edit')
                
def edit_user_password(request, id):
    return user_form(request, id, action_none='password')

def user_form(request, user_id=None, action_none=None):
    user_data = request.user
    data_table = User.objects.all().order_by('-id')

    if action_none == 'password' and user_id:
        user_update = User.objects.get(id=user_id)
        form = SetPasswordForm(user_update, request.POST or None)
        action = 'password'
    elif user_id:
        user_update = User.objects.get(id=user_id)
        form = UpdateUserForm(request.POST or None, instance=user_update)
        action = 'edit'
    else:
        form = InsertNewUserForm(request.POST or None)
        action = 'create'
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if action == 'create':
                user_log_activity(
                    user_data,
                    f'Novo usuário criado: {form.cleaned_data}',
                    get_client_ip(request)
                    )
                messages.success(request, "Novo usuário")
                print('Novo usuário criado com sucesso')
                return redirect('control_panel:users')
            elif action == 'edit':
                user_log_activity(
                    user_data,
                    f'Usuário {form.cleaned_data} alterado',
                    get_client_ip(request)
                    )
                messages.success(request, "Usuário editado")
                return redirect('control_panel:users')
            elif action == 'password':
                user_log_activity(
                    user_data,
                    f'Nova senha criada para usuário {form.cleaned_data}',
                    get_client_ip(request)
                    )
                messages.success(request, "Senha alterada")
                return redirect('control_panel:users')

    context = {
        'form': form,
        'action': action,
        'data_table': data_table
    }

    return render(request, 'pages/users.html', context)

@login_required
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
        messages.success(request, f'Usuário {user_obj} deletado')
        print(f'Usuário {user_obj} deletado')
        return redirect('control_panel:users')
    except Exception as error:
        messages.error(request, f'Erro ao deletar {user_obj}: {error}')
        print(f'Erro ao deletar {user_obj}: {error}')
    return redirect('control_panel:users')
    