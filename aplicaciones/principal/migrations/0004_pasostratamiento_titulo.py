# Generated by Django 3.1.1 on 2020-09-30 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_pasostratamiento_tratamiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='pasostratamiento',
            name='titulo',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
