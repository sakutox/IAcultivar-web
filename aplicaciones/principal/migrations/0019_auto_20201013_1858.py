# Generated by Django 3.1 on 2020-10-13 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0018_remove_enfermedadcultivo_danoscultivo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rango',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('rangoMinimo', models.DecimalField(decimal_places=0, max_digits=2)),
                ('rangoMaximo', models.DecimalField(decimal_places=0, max_digits=2)),
                ('nombre', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TipoTratamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=1000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='tablaimagenenfermedadcultivo',
            name='enfermedadCultivo',
        ),
        migrations.RemoveField(
            model_name='tratamiento',
            name='enfermedad',
        ),
        migrations.AddField(
            model_name='enfermedadpregunta',
            name='enfermedadCultivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='principal.enfermedadcultivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='enfermedadCultivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='principal.enfermedadcultivo'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='DanosEnfermedadCultivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('partePlanta', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=10000)),
                ('enfermedadCultivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.enfermedadcultivo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tablaimagenenfermedadcultivo',
            name='danosEnfermedadCultivo',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='principal.danosenfermedadcultivo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tratamiento',
            name='rango',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='principal.rango'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tratamiento',
            name='tipoDeTratamiento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='principal.tipotratamiento'),
        ),
    ]
