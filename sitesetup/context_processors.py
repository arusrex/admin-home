from .models import *
from django.utils.text import slugify

def site_settings(request):
    try:
        site_setup = SiteSetup.objects.first()
    except SiteSetup.DoesNotExist:
        site_setup = None
    
    context = {
        'site_setup': site_setup,
    }

    return context

def menu_settings(request):
    menu_principal = Menu.objects.all().order_by('nome')
    sub_menu = SubMenu.objects.all().order_by('nome')
    sub_sub_menu = SubSubMenu.objects.all().order_by('nome')

    if menu_principal.exists() or sub_menu.exists() or sub_sub_menu.exists():
        return {
            'menu_principal': menu_principal,
            'menu_secundario': sub_menu,
            'menu_terciario': sub_sub_menu,
        }
    else:
        return {
            'menu_principal': None,
            'menu_secundario': None,
            'menu_terciario': None,
        }
