# Generated by Django 4.2.8 on 2024-07-11 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='external_code',
        ),
    ]
