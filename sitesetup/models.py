from django.db import models
from django.contrib.auth.models import User

class SiteSetup(models.Model):
    
    nome = models.CharField(max_length=255, default='Administração')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome

class Menu(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.nome

class SubMenu(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='sub_menu')

    def __str__(self) -> str:
        return self.nome

class SubSubMenu(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True)
    sub_menu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, related_name='sub_sub_menu')

    def __str__(self) -> str:
        return self.nome
    
class EmailBackend(models.Model):
    email_host = models.CharField(max_length=255)
    email_port = models.IntegerField()
    email_use_tls = models.BooleanField(default=True)
    email_host_user = models.EmailField()
    email_host_password = models.CharField(max_length=255)
    default_from_email = models.EmailField(blank=True)

    def save(self, *args, **kwargs):
        if not self.default_from_email:
            self.default_from_email = self.email_host_user
        return super().save(*args, **kwargs)

class UserLogActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    additional_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.action} - {self.timestamp}' # type: ignore

