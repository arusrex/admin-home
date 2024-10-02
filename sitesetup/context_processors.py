from .models import *

def site_settings(request):
    try:
        site_setup = SiteSetup.objects.all()
    except SiteSetup.DoesNotExist:
        site_setup = None
    
    context = {
        'site_setup': site_setup,
    }

    return context

def menu_settings(request):
    try:
        menu = Menu.objects.all()
    except Menu.DoesNotExist:
        menu = None
        print('Erro: Não existem menus, ou não foram cadastrados')

    try:
        sub_menu = SubMenu.objects.all()
    except SubMenu.DoesNotExist:
        sub_menu = None
        print('Erro: Não existem sub-menus, ou não foram cadastrados')
    try:
        sub_sub_menu = SubSubMenu.objects.all()
    except SubSubMenu.DoesNotExist:
        sub_sub_menu = None
        print('Erro: Não existem sub-sub-menus, ou não foram cadastrados')