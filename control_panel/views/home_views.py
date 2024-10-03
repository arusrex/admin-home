from django.shortcuts import render, redirect
from sitesetup.models import SiteSetup, Menu, SubMenu, SubSubMenu
from sitesetup.forms import SiteSetupForm, MenuForm, SubMenuForm, SubSubMenuForm

def home(request):
    return render(request, 'pages/index.html')

def site_setup(request):
    obj = SiteSetup.objects.first()
    
    if request.method == 'POST':
        form_site_setup = SiteSetupForm(request.POST, instance=obj)

        try:
            if form_site_setup.is_valid():
                form_site_setup.save()
                print(f'{form_site_setup} - Registro salvo com sucesso')
                return redirect('control_panel:home')
        except Exception as error:
            print(f'Registro não realizado conforme o erro: {error}')
            return redirect('control_home:home')
    
    else:
        form_site_setup = SiteSetupForm(instance=obj)

        context = {
            'form': form_site_setup,
        }

    return render(request, 'pages/site_setup.html', context)

