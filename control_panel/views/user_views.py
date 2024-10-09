from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from control_panel.forms import CustomUserUpdateForm
from sitesetup.context_processors import user_log_activity


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
                    request.META.get('REMOTE_ADDR')
                    )
                return password_change(request, user_data, new_password1)
            else:
                user_log_activity(
                    user_data,
                    'Senha diferentes ao alterar',
                    request.META.get('REMOTE_ADDR')
                    )
                print(f'Senhas incomaptíveis: {new_password1} é diferente de {new_password2}')
                return redirect('control_panel:user_data')
        else:
            form = CustomUserUpdateForm(request.POST, instance=user_data)
            if form.is_valid():
                form.save()
                changed_values = [field for field in form.changed_data]
                # user_log_activity(
                # user_data,
                # f'Novos dados: {form.values()}',
                # request.META.get('REMOTE_ADDR')
                # )
                user_log_activity(
                    user_data,
                    f'Novos dados: {changed_values}',
                    request.META.get('REMOTE_ADDR')
                    )
                print('Dados de usuário alterados com sucesso')
                return redirect('control_panel:user_data')
            else:
                user_log_activity(
                    user_data,
                    f'Erro nos dados de usuário',
                    request.META.get('REMOTE_ADDR')
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
