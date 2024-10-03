from django.shortcuts import render, redirect
from sitesetup.models import SiteSetup, Menu, SubMenu, SubSubMenu
from sitesetup.forms import SiteSetupForm, MenuForm, SubMenuForm, SubSubMenuForm

def home(request):
    return render(request, 'pages/index.html')

def site_setup(request):
    obj = SiteSetup.objects.first()
    if request.method == 'POST':
        form_site_setup = SiteSetupForm(request.POST, request.FILES, instance=obj)
        try:
            if form_site_setup.is_valid():
                form_site_setup.save()
                print(f'{form_site_setup} - Registro salvo com sucesso')
                return redirect('control_panel:site_setup')
        except Exception as error:
            print(f'Registro não realizado conforme o erro: {error}')
            return redirect('control_home:home')
    else:
        form_site_setup = SiteSetupForm(instance=obj)
        context = {
            'form': form_site_setup,
        }
    return render(request, 'pages/site_setup.html', context)


def main_menus(request):
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
    else:
        form = MenuForm()
        context = {
            'form': form,
        }

    return render(request, 'pages/menu_setup.html', context)

def edit_main_menu(request, id):
    obj = Menu.objects.get(id=id)
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
    else:
        form = MenuForm(instance=obj)
        context = {
            'form': form,
        }
    return render(request, 'pages/menu_setup.html', context)

def delete_main_menu(request, id):
    obj = Menu.objects.get(id=id)
    try:
        if obj:
            obj.delete()
            print(f'{obj} - Menu deletado com sucesso')
    except Exception as error:
        print(f'Erro ao deletar menu: {error}')
    return redirect('control_panel:main_menus')

