# Generated by Django 5.1.1 on 2024-10-03 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesetup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='link',
            field=models.URLField(blank=True, default='S/D', null=True),
        ),
        migrations.AlterField(
            model_name='submenu',
            name='link',
            field=models.URLField(blank=True, default='S/D', null=True),
        ),
        migrations.AlterField(
            model_name='subsubmenu',
            name='link',
            field=models.URLField(blank=True, default='S/D', null=True),
        ),
    ]