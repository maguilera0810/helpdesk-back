# Generated by Django 4.2.8 on 2024-10-13 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_rename_code_custompermission_key_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomPermission',
            new_name='Permission',
        ),
    ]