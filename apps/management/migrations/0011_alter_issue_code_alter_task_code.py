# Generated by Django 4.2.8 on 2024-08-28 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0010_remove_issue_requesting_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='code',
            field=models.CharField(db_index=True, editable=False, help_text='max_length= len(model_name) + 33', max_length=38, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='code',
            field=models.CharField(db_index=True, editable=False, help_text='max_length= len(model_name) + 33', max_length=37, unique=True),
        ),
    ]
