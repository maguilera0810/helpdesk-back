# Generated by Django 4.2.8 on 2024-10-14 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0011_rename_value_priority_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='priority',
            name='group',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='priority',
            name='icon',
            field=models.TextField(blank=True),
        ),
    ]
