# Generated by Django 3.2.8 on 2021-10-27 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_alter_settings_value'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Settings',
            new_name='FileSettings',
        ),
    ]
