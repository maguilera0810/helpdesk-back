# Generated by Django 4.2.8 on 2024-08-23 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_issuefile_created_by_alter_scheduledtask_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='code',
            field=models.CharField(db_index=True, default='', editable=False, max_length=37, unique=True),
            preserve_default=False,
        ),
    ]