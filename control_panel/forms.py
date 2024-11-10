from typing import Any
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError

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

class InsertNewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']

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
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['username'].help_text = (
            '''
            <ul>
                <li>Mínimo 5 caracteres</li>
                <li>Máximo 100 caracteres</li>
                <li>Letras e números</li>
            </ul>
            '''
        )
        self.fields['first_name'].help_text = (
            'Digite seu nome'
        )
        self.fields['last_name'].help_text = (
            'Digite seu sobrenome'
        )
        self.fields['email'].help_text = (
            '''
            <ul>
                <li>Digite um email válido</li>
                <li>Exemplo: email@exemplo.com</li>
            </ul>
            '''
        )
        self.fields['is_active'].help_text = (
            '<p>Selecione para ativar ou desativar o usuário</p>'
        )
        self.fields['is_staff'].help_text = (
            '<p>Selecione se o usuário receberá previlégios de colaborador</p>'
        )
        self.fields['is_superuser'].help_text = (
            '<p>Selecione se o usuário receberá previlégios de administrador</p>'
        )


    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso')
        
        if len(username) < 5 or len(username) > 100:
            raise forms.ValidationError('O nome de usuário deve ter pelo menos 5 caracteres e menos que 100')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Este email já está em uso')
        
        if '@' not in email and '.' not in email:
            raise forms.ValidationError('Digite um email válido')
        
        if email.endswith('@exemplo.com'):
            raise forms.ValidationError('Não é possível criar contas com o domínio exemplo.com')
        
        return email
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2:
            if password1 != password2:
                raise ValidationError("As senhas não coincidem.")
            
            if len(password1) < 8: # type: ignore
                raise forms.ValidationError('A senha deve ter pelo menos 8 caracteres')
        
            if not any(char.isdigit() for char in password1):
                raise forms.ValidationError('A senha deve conter pelo menos um número')
            
            if ' ' in password1:
                raise forms.ValidationError('A senha não pode conter espaços')
            
            if not any(char.isupper() for char in password1):
                raise forms.ValidationError('A senha deve conter pelo menos uma letra maiúscula')
            
            if not any(char.islower() for char in password1):
                raise forms.ValidationError('A senha deve conter pelo menos uma letra minúscula')
            
            if not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/`~" for char in password1):
                raise ValidationError('A senha deve conter pelo menos um caractere especial')
        
        return cleaned_data
    
class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser']

        labels = {
            'username': 'Nome de usuário',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email': 'Email',
            'is_active': 'Ativo',
            'is_staff': 'Colaborador',
            'is_superuser': 'Administrador',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
        self.fields['username'].help_text = (
            '''
            <ul>
                <li>Mínimo 5 caracteres</li>
                <li>Máximo 100 caracteres</li>
                <li>Letras e números</li>
            </ul>
            '''
        )
        self.fields['first_name'].help_text = (
            'Digite seu nome'
        )
        self.fields['last_name'].help_text = (
            'Digite seu sobrenome'
        )
        self.fields['email'].help_text = (
            '''
            <ul>
                <li>Digite um email válido</li>
                <li>Exemplo: email@exemplo.com</li>
            </ul>
            '''
        )
        self.fields['is_active'].help_text = (
            '<p>Selecione para ativar ou desativar o usuário</p>'
        )
        self.fields['is_staff'].help_text = (
            '<p>Selecione se o usuário receberá previlégios de colaborador</p>'
        )
        self.fields['is_superuser'].help_text = (
            '<p>Selecione se o usuário receberá previlégios de administrador</p>'
        )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Este nome de usuário já está em uso')
        
        if len(username) < 5 and len(username) > 100:
            raise forms.ValidationError('O nome de usuário deve ter pelo menos 5 caracteres e menos que 100')
        
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(id=self.instance.id).exists():
            raise forms.ValidationError('Este email já está em uso')
        
        if '@' not in email and '.' not in email:
            raise forms.ValidationError('Digite um email válido')
        
        if email.endswith('@exemplo.com'):
            raise forms.ValidationError('Não é possível criar contas com o domínio exemplo.com')
        
        return email