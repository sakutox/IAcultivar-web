# Generated by Django 3.1 on 2020-10-14 12:55

import aplicaciones.principal.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0019_auto_20201013_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablaimagentratamiento',
            name='URL',
        ),
        migrations.AddField(
            model_name='tablaimagentratamiento',
            name='imagen',
            field=models.ImageField(blank=True, upload_to=aplicaciones.principal.models.TablaImagenTratamiento.cargar_imagen_tratamiento),
        ),
    ]
