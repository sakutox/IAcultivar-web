# Generated by Django 3.1.1 on 2020-09-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivo',
            name='idCultivo',
        ),
        migrations.RemoveField(
            model_name='enfermedad',
            name='idEnfermedad',
        ),
        migrations.AddField(
            model_name='cultivo',
            name='id',
            field=models.AutoField(auto_created=True, default=None, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='enfermedad',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]