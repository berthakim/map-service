# Generated by Django 3.1.4 on 2021-01-30 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foliums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='light',
            old_name='sunet',
            new_name='sunset',
        ),
    ]
