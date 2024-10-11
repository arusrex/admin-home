from .models import SiteSetup, Menu, SubMenu, SubSubMenu, EmailBackend
from django import forms

class SiteSetupForm(forms.ModelForm):
    class Meta:
        model = SiteSetup
        fields = '__all__'

        labels = {
            'nome': 'Nome',
            'logo': 'Logotipo',
            'is_active': 'Publicado',
            'favicon': 'Ícone do sistema (.png)',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'logo': forms.ClearableFileInput(attrs={'class':'form-control form-control-sm'}),
            'favicon': forms.ClearableFileInput(attrs={'class':'form-control form-control-sm', 'accept':".png"}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = '__all__'

        labels = {
            'nome': 'Nome',
            'link': 'Link/URL'
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'})
        }

class SubMenuForm(forms.ModelForm):
    class Meta:
        model = SubMenu
        fields = '__all__'

        labels = {
            'nome': 'Nome',
            'link': 'Link/URL',
            'menu': 'Menu Correspondente',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'menu': forms.Select(attrs={'class':'form-select'}),
        }

class SubSubMenuForm(forms.ModelForm):
    class Meta:
        model = SubSubMenu
        fields = '__all__'
        
        labels = {
            'nome': 'Nome',
            'link': 'Link/URL',
            'sub_menu': 'sub_menu',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.URLInput(attrs={'class':'form-control'}),
            'sub_menu': forms.Select(attrs={'class':'form-select'}),
        }

class EmailBackendForm(forms.ModelForm):
    class Meta:
        model = EmailBackend
        fields = '__all__'

        labels = {
            'email_host': 'Servidor SMTP',
            'email_port': 'Porta SMTP',
            'email_use_tls': 'Habilita criptografia TLS',
            'email_host_user': 'Digite o email',
            'email_host_password': 'Senha do email',
            'default_from_email': 'O endereço "De" padrão para os e-mails enviados',
        }

        widgets = {
            'email_host': forms.TextInput(attrs={'class':'form-control'}),
            'email_port': forms.NumberInput(attrs={'class':'form-control'}),
            'email_use_tls': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'email_host_user': forms.EmailInput(attrs={'class': 'form-control'}),
            'email_host_password': forms.PasswordInput(attrs={'class':'form-control'}),
            'default_from_email': forms.EmailInput(attrs={'class':'form-control'}),
        }
