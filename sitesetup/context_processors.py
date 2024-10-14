from .models import *


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
    
def user_log_activity(user, action, ip_address=None, additional_info=None):
    UserLogActivity.objects.create(
        user=user,
        action=action,
        ip_address=ip_address,
        additional_info=additional_info,
    )
    print(f'Atividade registrado {action}')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
