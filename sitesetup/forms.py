from .models import SiteSetup, Menu, SubMenu, SubSubMenu
from django import forms

class SiteSetupForm(forms.ModelForm):
    class Meta:
        model = SiteSetup
        fields = '__all__'

        labels = {
            'nome': 'Nome',
            'logo': 'Logotipo',
            'is_active': 'Publicado',
        }

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'logo': forms.FileInput(attrs={'class':'form-control form-control-sm'}),
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

