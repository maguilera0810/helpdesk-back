# Generated by Django 4.2.8 on 2024-10-09 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0009_priority'),
        ('management', '0018_remove_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='priority',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='common.priority'),
        ),
    ]
