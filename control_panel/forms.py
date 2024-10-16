from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        
        labels = {
            'username':'Usuário',
            'first_name':'Nome',
            'last_name':'Sobrenome',
            'email':'Endereço de email',
        }
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

class InsertNewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']

        # password1 = forms.CharField(
        # label="Senha",
        # widget=forms.PasswordInput(attrs={'class': 'form-control'})
        # )
        # password2 = forms.CharField(
        #     label="Confirmação da Senha",
        #     widget=forms.PasswordInput(attrs={'class': 'form-control'})
        # )

        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'password1': 'Senha',
            'password2': 'Confirmação da senha',
            'is_active': 'Ativo',
            'is_staff': 'Colaborador',
            'is_superuser': 'Administrador',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            # 'password1': forms.PasswordInput(attrs={'class':'form-control'}),
            # 'password2': forms.PasswordInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }