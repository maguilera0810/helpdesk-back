# Generated by Django 4.2.8 on 2024-09-16 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0015_task_end_at_task_start_at_delete_taskschedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='end_date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='plan',
            name='start_date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='scheduledtask',
            name='end_date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='scheduledtask',
            name='start_date',
            field=models.DateField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='end_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='start_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True),
        ),
    ]