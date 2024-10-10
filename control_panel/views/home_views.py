from django.shortcuts import render, redirect
from sitesetup.models import SiteSetup, Menu, SubMenu, SubSubMenu, EmailBackend
from sitesetup.forms import SiteSetupForm, MenuForm, SubMenuForm, SubSubMenuForm, EmailBackendForm
from django.contrib.auth.decorators import login_required
from sitesetup.context_processors import user_log_activity
from django.core.files.storage import default_storage
import subprocess


@login_required
def home(request):
    return render(request, 'pages/index.html')

@login_required
def site_setup(request):
    user_data = request.user
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
                    changed_fields = [field for field in form_email_backend.changed_data]
                    user_log_activity(
                        user_data,
                        f'Dados novos de email backend: {changed_fields}',
                        request.META.get('REMOTE_ADDR'),
                    )
                    print('Dados de email backend salvos')
                    return redirect('control_panel:site_setup')
                else:
                    print('Erro ao salvar os dados do email backend')
                    user_log_activity(
                        user_data,
                        'Error ao salvar dados do email backend',
                        request.META.get('REMOTE_ADDR'),
                    )
                return redirect('control_panel:site_setup')
            except Exception as error:
                print(f'Erro ao registrar dados de email backend: {error}')
                return redirect('control_panel:site_setup')
        else:
            form_site_setup = SiteSetupForm(request.POST, request.FILES, instance=obj)
            try:
                if form_site_setup.is_valid():
                    form_site_setup.save()
                    changed_fields = [field for field in form_site_setup.changed_data]
                    user_log_activity(
                        user_data,
                        f'Dados novos do site: {changed_fields}',
                        request.META.get('REMOTE_ADDR'),
                    )
                    print(f'Registro salvo com sucesso')
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
    user_data = request.user
    form = MenuForm()
    if request.method == 'POST':
        form = MenuForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                user_log_activity(
                    user_data,
                    'Menu registrado',
                    request.META.get('REMOTE_ADDR'),
                )
                print(f'Registro salvo com sucesso')
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
    user_data = request.user
    obj = Menu.objects.get(id=id)
    form = MenuForm(instance=obj)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=obj)
        try:
            if form.is_valid():
                form.save()
                changed_fields = [field for field in form.changed_data]
                user_log_activity(
                    user_data,
                    f'Menu editado: {changed_fields}',
                    request.META.get('REMOTE_ADDR'),
                )
                print(f'Registro salvo com sucesso')
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
    user_data = request.user
    try:
        obj = Menu.objects.get(id=id)
        obj_delete = obj.delete()
        print(f'{obj_delete} - Menu deletado com sucesso')
        user_log_activity(
            user_data,
            f'Menu deletado: {obj_delete}',
            request.META.get('REMOTE_ADDR'),
        )
        return redirect('control_panel:main_menus')
    except Exception as error:
        print(f'Erro ao deletar menu: {error}')
        return redirect('control_panel:main_menus')

@login_required
def sub_menus(request):
    user_data = request.user
    form = SubMenuForm()
    if request.method == 'POST':
        form = SubMenuForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                user_log_activity(
                    user_data,
                    'Categoria criada',
                    request.META.get('REMOTE_ADDR'),
                )
                print(f'Sub menu cadastrado')
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
    user_data = request.user
    obj = SubMenu.objects.get(id=id)
    form = SubMenuForm(instance=obj)
    if request.method == 'POST':
        form = SubMenuForm(request.POST, instance=obj)
        try:
            if form.is_valid():
                form.save()
                changed_fields = [field for field in form.changed_data]
                user_log_activity(
                    user_data,
                    f'Categoria alterada: {changed_fields}',
                    request.META.get('REMOTE_ADDR'),
                )
                print(f'Editado com sucesso')
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
    user_data = request.user
    try:
        obj = SubMenu.objects.get(id=id)
        obj_delete = obj.delete()
        print(f'{obj_delete} - Deletado com sucesso')
        user_log_activity(
            user_data,
            f'Categoria deletada: {obj_delete}',
            request.META.get('REMOTE_ADDR'),
        )
        return redirect('control_panel:sub_menus')
    except Exception as error:
        print(f'Erro ao deletar sub-menu: {error}')
        return redirect('control_panel:sub_menus')

@login_required
def sub_sub_menus(request):
    user_data = request.user
    form = SubSubMenuForm()
    if request.method == 'POST':
        form = SubSubMenuForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                user_log_activity(
                    user_data,
                    'Sub-Categoria criada',
                    request.METS.get('REMOTE_ADDR'),
                )
                print(f'Sub-sub-menu cadastrado com sucesso')
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
    user_data = request.user
    obj = SubSubMenu.objects.get(id=id)
    form = SubSubMenuForm(instance=obj)
    if request.method == 'POST':
        form = SubSubMenuForm(request.POST, instance=obj)
        try:
            if form.is_valid():
                form.save()
                changed_fields = [field for field in form.changed_data]
                user_log_activity(
                    user_data,
                    f'Sub-Categoria editada: {changed_fields}',
                    request.META.get('REMOTE_ADDR'),
                )
                print(f'Sub-sub-menu editado com sucesso')
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
    user_data = request.user
    try:
        obj = SubSubMenu.objects.get(id=id)
        obj_delete = obj.delete()
        print(f'{obj_delete} - Sub-sub-menu deletado com sucesso')
        user_log_activity(
            user_data,
            f'Sub-Categoria deletada: {obj_delete}',
            request.META.get('REMOTE_ADDR'),
        )
        return redirect('control_panel:sub_sub_menus')
    except Exception as error:
        print(f'Erro ao deletar sub-sub-menu: {error}')
        return redirect('control_panel:sub_sub_menus')

def backups(request):
    return render(request, 'pages/db_backup.html')

def db_backup(request):
    user_data = request.user
    op_system = request.GET.get('op_system')
    try:
        if op_system == '1':
            subprocess.call([r'venv/bin/python3', 'manage.py', 'dbbackup'])
            print(f'Backup realizado com sucesso')
            user_log_activity(
                user_data,
                'Execução de backup do sistema',
                request.META.get('REMOTE_ADDR'),
            )
        else:
            subprocess.call([r'venv\Scripts\python', 'manage.py', 'dbbackup'])
            print(f'Backup realizado com sucesso')
            user_log_activity(
                user_data,
                'Execução de backup do sistema',
                request.META.get('REMOTE_ADDR'),
            )
    except Exception as error:
        print(f'Erro ao realizar backup do sistema: {error}')

    return redirect('control_panel:backups')

def db_backup_restore(request):
    user_data = request.user
    op_system = request.GET.get('op_system')
    if request.method == 'POST' and request.FILES['backup_file']:
        backup_file = request.FILES['backup_file']
        try:
            if op_system == '1':
                path = default_storage.save('db_backups/' + backup_file.name, backup_file)
                subprocess.call([r'venv/bin/python3', 'manage.py', 'dbrestore', '--input-filename=' + path])
                print('Restauração de backup realizada com sucesso')
                user_log_activity(
                    user_data,
                    'Executado restauração de backup',
                    request.META.get('REMOTE_ADDR'),
                )
            else:
                path = default_storage.save('db_backups/' + backup_file.name, backup_file)
                subprocess.call([r'venv\Scripts\python', 'manage.py', 'dbrestore', '--input-filename=' + path])
                print('Restauração de backup realizada com sucesso')
                user_log_activity(
                    user_data,
                    'Executado restauração de backup',
                    request.META.get('REMOTE_ADDR'),
                )
        except Exception as error:
            print(f'Erro ao realizar restauração de backup: {error}')
    return redirect('control_panel:backups')

