from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from control_panel.forms import CustomUserUpdateForm, UserCreationForm, InsertNewUserForm, UpdateUserForm
from sitesetup.context_processors import user_log_activity
from django.contrib.auth.models import User
from sitesetup.context_processors import get_client_ip
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm

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

@login_required
def users(request):
    user_data = request.user
    users = User.objects.all().order_by('first_name')
    if request.method == 'POST':
        form = InsertNewUserForm(request.POST)

        if form.is_valid():
            print('Form valid')
            form.save()
            messages.success(request, 'Novo usuário criado com sucesso')
            print('Novo usuário criado com sucesso')
            return redirect('control_panel:users')
        else:
            print(form.errors)

    form = InsertNewUserForm()

    context = {
        'data_table': users,
        'form': form,
    }

    return render(request, 'pages/users.html', context)

@login_required
def edit_user(request, id):
    user_data = request.user
    user_obj = User.objects.get(id=id)
    users = User.objects.all().order_by('first_name')

    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user_obj)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Senha de usuário {user_obj} alterada')
            print(f'Senha de usuário {user_obj} alterada')
            user_log_activity(
                user_data,
                f'Senha de usuário ({user_obj}) alterada',
                get_client_ip(request),
            )
            return redirect('control_panel:users')

            # new_password1 = request.POST.get('password1')
            # new_password2 = request.POST.get('password2')
            # if new_password1:
            #     if new_password1 != new_password2:
            #         print('Senhas não coincidem')
            #     else:
            #         form.save(commit=False)
            #         user_obj.set_password(new_password1)
            #         user_obj.save()
            #         user_log_activity(
            #             user_data,
            #             f'Senha de usuário ({user_obj}) alterada',
            #             get_client_ip(request),
            #         )
            #         messages.success(request, f'Senha de usuário {user_obj} alterada')
            #         print(f'Senha de usuário {user_obj} alterada')
            #         return redirect('control_panel:users')
            # else:
            #     form.save()
            #     user_log_activity(
            #         user_data,
            #         f'Usuário ({user_obj}) editado',
            #         get_client_ip(request),
            #     )
            #     messages.success(request, 'Usuário editado com sucesso')
            #     print('Usuário editado com sucesso')
            #     return redirect('control_panel:users')
        else:
            print(form.errors)

    else:
        form = UpdateUserForm(instance=user_obj)

    context = {
        'data_table': users,
        'form': form,
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
    