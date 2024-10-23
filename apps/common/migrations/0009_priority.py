# Generated by Django 4.2.8 on 2024-10-09 00:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_alter_category_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
                ('icon', models.CharField(blank=True, max_length=30)),
                ('color', models.CharField(help_text='Formato hexadecimal (ej. #FF00AA)', max_length=7, validators=[django.core.validators.RegexValidator(code='invalid_color', message='El color debe ser un valor hexadecimal válido', regex='^#[0-9A-Fa-f]{6}$')])),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
