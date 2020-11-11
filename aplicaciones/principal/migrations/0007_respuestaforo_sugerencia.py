# Generated by Django 3.1.1 on 2020-09-30 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0006_preguntaforo_usuarioforo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('cuerpo', models.CharField(max_length=500)),
                ('puntuacion', models.DecimalField(decimal_places=2, max_digits=2)),
                ('usuarioForo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.usuarioforo')),
            ],
        ),
        migrations.CreateModel(
            name='RespuestaForo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('textoRespuesta', models.CharField(max_length=1000)),
                ('apropiada', models.BooleanField(verbose_name=True)),
                ('usuarioForo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.usuarioforo')),
            ],
        ),
    ]