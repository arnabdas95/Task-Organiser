# Generated by Django 3.0.4 on 2020-04-12 04:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_group', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task_Groups',
            new_name='Catagories',
        ),
        migrations.RenameField(
            model_name='catagories',
            old_name='group_name',
            new_name='catagories_name',
        ),
    ]
