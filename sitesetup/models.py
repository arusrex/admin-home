from django.db import models

class SiteSetup(models.Model):
    
    nome = models.CharField(max_length=255, default='Administração')
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.nome

class Menu(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True, default='http://exemplo.com')

    def __str__(self) -> str:
        return self.nome

class SubMenu(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True, default='http://exemplo.com')
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='sub_menu')

    def __str__(self) -> str:
        return self.nome

class SubSubMenu(models.Model):
    nome = models.CharField(max_length=255)
    link = models.URLField(blank=True, null=True, default='http://exemplo.com')
    sub_menu = models.ForeignKey(SubMenu, on_delete=models.CASCADE, related_name='sub_sub_menu')

    def __str__(self) -> str:
        return self.nome
