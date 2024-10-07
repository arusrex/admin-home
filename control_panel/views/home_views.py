from django.shortcuts import render, redirect
from sitesetup.models import SiteSetup, Menu, SubMenu, SubSubMenu, EmailBackend
from sitesetup.forms import SiteSetupForm, MenuForm, SubMenuForm, SubSubMenuForm, EmailBackendForm
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'pages/index.html')

@login_required
def site_setup(request):
    obj = SiteSetup.objects.first()
    obj_email_backend = EmailBackend.objects.first()
    form_site_setup = SiteSetupForm(instance=obj)
    form_email_backend = EmailBackendForm(instance=obj_email_backend)
    if request.method == 'POST':
        if 'email_backend_form' in request.POST:
            form_email_backend = EmailBackendForm(request.POST, instance=obj_email_backend)
            try:
                if form_email_backend.is_valid():
                    form_email_backend.save()
                    print('Dados de email backenda salvos')
                    return redirect('control_panel:site_setup')
                else:
                    print('Erro ao salvar os dados do email backend')
                return redirect('control_panel:site_setup')
            except Exception as error:
                print(f'Erro ao registrar dados de email backend: {error}')
                return redirect('control_panel:site_setup')
        else:
            form_site_setup = SiteSetupForm(request.POST, request.FILES, instance=obj)
            try:
                if form_site_setup.is_valid():
                    form_site_setup.save()
                    print(f'{form_site_setup} - Registro salvo com sucesso')
                    return redirect('control_panel:site_setup')
            except Exception as error:
                print(f'Registro não realizado conforme o erro: {error}')
                return redirect('control_home:home')

    context = {
        'form': form_site_setup,
        'form_email_backend': form_email_backend,
    }
    return render(request, 'pages/site_setup.html', context)



@login_required
def main_menus(request):
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                print(f'{form} Registro salvo com sucesso')
                return redirect('control_panel:main_menus')
        except Exception as error:
            print(f'Erro ao registrar o menu: {error}')
            return redirect('control_panel:main_menus')
    context = {
        'form': form,
    }
    return render(request, 'pages/menu_setup.html', context)

@login_required
def edit_main_menu(request, id):
    obj = Menu.objects.get(id=id)
    form = MenuForm(instance=obj)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=obj)
        try:
            if form.is_valid():
                form.save()
                print(f'{form} - Registro salvo com sucesso')
                return redirect('control_panel:main_menus')
        except Exception as error:
            print(f'Erro ao salvar o menu: {error}')
            return redirect('control_panel:main_menus')
    context = {
        'form': form,
    }
    return render(request, 'pages/menu_setup.html', context)

@login_required
def delete_main_menu(request, id):
    try:
        obj = Menu.objects.get(id=id)
        obj.delete()
        print(f'{obj} - Menu deletado com sucesso')
        return redirect('control_panel:main_menus')
    except Exception as error:
        print(f'Erro ao deletar menu: {error}')
        return redirect('control_panel:main_menus')

@login_required
def sub_menus(request):
    form = SubMenuForm()
    if request.method == 'POST':
        form = SubMenuForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                print(f'{form} - Sub menu cadastrado')
                return redirect('control_panel:sub_menus')
        except Exception as error:
            print(f'Erro ao cadastrar sub-menu: {error}')
            return redirect('control_panel:sub_menus')
    context = {
        'form': form,
    }
    return render(request, 'pages/sub_menu.html', context)

@login_required
def edit_sub_menu(request, id):
    obj = SubMenu.objects.get(id=id)
    form = SubMenuForm(instance=obj)
    if request.method == 'POST':
        form = SubMenuForm(request.POST, instance=obj)
        try:
            if form.is_valid():
                form.save()
                print(f'{form} - Cadastrado com sucesso')
                return redirect('control_panel:sub_menus')
        except Exception as error:
            print(f'Erro ao cadastrar sub-menu: {error}')
            return redirect('control_panel:sub_menus')
    context = {
        'form': form,
    }
    return render(request, 'pages/sub_menu.html', context)

@login_required
def delete_sub_menu(request, id):
    try:
        obj = SubMenu.objects.get(id=id)
        obj.delete()
        print(f'{obj} - Deletado com sucesso')
        return redirect('control_panel:sub_menus')
    except Exception as error:
        print(f'Erro ao deletar sub-menu: {error}')
        return redirect('control_panel:sub_menus')

@login_required
def sub_sub_menus(request):
    form = SubSubMenuForm()
    if request.method == 'POST':
        form = SubSubMenuForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                print(f'{form} - Sub-sub-menu cadastrado com sucesso')
                return redirect('control_panel:sub_sub_menus')
        except Exception as error:
            print(f'Erro ao cadastrar sub-sub-menu: {error}')
            return redirect('control_panel:sub_sub_menus')
    context = {
        'form': form,
    }
    return render(request, 'pages/sub_sub_menus.html', context)

@login_required
def edit_ss_menus(request, id):
    obj = SubSubMenu.objects.get(id=id)
    form = SubSubMenuForm(instance=obj)
    if request.method == 'POST':
        form = SubSubMenuForm(request.POST, instance=obj)
        try:
            if form.is_valid():
                form.save()
                print(f'{form} - Sub-sub-menu cadastrado com sucesso')
                return redirect('control_panel:sub_sub_menus')
        except Exception as error:
            print(f'Erro ao cadastrar sub-sub-menu: {error}')
            return redirect('control_panel:sub_sub_menus')
    context = {
        'form': form,
    }
    return render(request, 'pages/sub_sub_menus.html', context)

@login_required
def delete_ss_menus(request, id):
    try:
        obj = SubSubMenu.objects.get(id=id)
        obj.delete()
        print(f'{obj} - Sub-sub-menu deletado com sucesso')
        return redirect('control_panel:sub_sub_menus')
    except Exception as error:
        print(f'Erro ao deletar sub-sub-menu: {error}')
        return redirect('control_panel:sub_sub_menus')