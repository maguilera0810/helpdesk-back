# Generated by Django 4.2.8 on 2024-10-12 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_role_permissions_alter_role_users'),
    ]

    operations = [
        migrations.RenameField(
            model_name='custompermission',
            old_name='code',
            new_name='key',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='code',
            new_name='key',
        ),
    ]
