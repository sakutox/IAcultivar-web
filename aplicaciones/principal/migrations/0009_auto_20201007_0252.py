# Generated by Django 3.1 on 2020-10-07 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0008_remove_cultivo_variedadescultivo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enfermedad',
            name='cultivo',
        ),
        migrations.AddField(
            model_name='enfermedad',
            name='dañosCultivo',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='descripcion',
            field=models.CharField(default=None, max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='tipoDeTratamiento',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
