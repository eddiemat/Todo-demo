# Generated by Django 4.2.3 on 2023-07-05 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_alter_task_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='description',
        ),
    ]
