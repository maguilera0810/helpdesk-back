# Generated by Django 4.2.8 on 2024-10-06 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0007_category_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='categorytype',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]