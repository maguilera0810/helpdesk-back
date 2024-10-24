# Generated by Django 4.2.8 on 2024-08-21 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_category_tag'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('management', '0006_alter_task_responsible_alter_task_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('to_do', 'to_do'), ('in_progress', 'in_progress'), ('blocked', 'blocked'), ('to_validate', 'to_validate'), ('completed', 'completed')], default='to_do', max_length=50)),
                ('contact_email', models.CharField(blank=True, max_length=100)),
                ('contact_phone', models.CharField(blank=True, max_length=10)),
                ('categories', models.ManyToManyField(blank=True, related_name='issues', to='common.category')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='created_issues', to=settings.AUTH_USER_MODEL)),
                ('requesting_unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='management.requestingunit')),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='issue', to='management.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IssueFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('file', models.CharField(max_length=200)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='management.issue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Request',
        ),
    ]
