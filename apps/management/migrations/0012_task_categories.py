# Generated by Django 4.2.8 on 2024-09-01 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_alter_category_code_alter_skill_code_alter_tag_code'),
        ('management', '0011_alter_issue_code_alter_task_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='categories',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='common.category'),
        ),
    ]
