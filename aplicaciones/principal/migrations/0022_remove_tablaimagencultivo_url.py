# Generated by Django 3.1 on 2020-10-28 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0021_auto_20201028_0552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablaimagencultivo',
            name='url',
        ),
    ]
