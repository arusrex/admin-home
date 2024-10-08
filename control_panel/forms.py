from django.contrib.auth.models import User
from django import forms

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
