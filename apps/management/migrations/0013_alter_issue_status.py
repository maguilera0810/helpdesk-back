# Generated by Django 4.2.8 on 2024-09-02 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0012_task_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('received', 'received'), ('task_created', 'task_created'), ('rejected', 'rejected'), ('to_validate', 'to_validate'), ('completed', 'completed')], default='received', max_length=50),
        ),
    ]
