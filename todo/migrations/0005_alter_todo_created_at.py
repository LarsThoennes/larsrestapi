# Generated by Django 5.1 on 2024-08-16 11:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_rename_ftitle_todo_title_alter_todo_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date'),
        ),
    ]
