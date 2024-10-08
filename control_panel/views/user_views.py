from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from control_panel.forms import CustomUserUpdateForm


@login_required
def user_data(request):
    user_data = request.user
    form = CustomUserUpdateForm(instance=user_data)
    if request.method == 'POST':
        if 'password_change' in request.POST:
            new_password1 = request.POST.get('new_password1')
            new_password2 = request.POST.get('new_password2')
            password_change(user_data, new_password1, new_password2)
        else:
            form = CustomUserUpdateForm(request.POST, instance=user_data)
            if form.is_valid():
                form.save()
                print('Dados de usuário alterados com sucesso')
                return redirect('control_panel:logout')
            else:
                print(f'Erro ao salvar os dados de usuário: {form.errors}')
                return redirect('control_panel:user_data')

    context = {
        'form':form,
    }
    return render(request, 'pages/user_data.html', context)

def password_change(user_data, pass1, pass2):
    print(user_data.first_name, pass1, pass2)
    if pass1 != pass2:
        print(f'Senhas incomaptíveis: {pass1} é diferente de {pass2}')
        return redirect('control_panel:user_data')
    user_data.set_password(pass1)
    user_data.save()
    return redirect('control_panel:logout')
