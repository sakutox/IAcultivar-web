# Generated by Django 3.1 on 2020-10-08 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_auto_20201008_0127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfermedad',
            name='danosCultivo',
        ),
    ]