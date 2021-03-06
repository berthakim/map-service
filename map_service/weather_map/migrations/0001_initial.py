# Generated by Django 3.1.4 on 2021-01-11 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
        migrations.CreateModel(
            name='Pop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_pop', models.CharField(max_length=25)),
                ('img_pop', models.FileField(default='', upload_to='')),
                ('text_pop', models.CharField(max_length=1000)),
            ],
        ),
    ]
