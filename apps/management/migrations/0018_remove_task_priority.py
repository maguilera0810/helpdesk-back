# Generated by Django 4.2.8 on 2024-10-09 00:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0017_alter_issue_description_alter_issuefile_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='priority',
        ),
    ]