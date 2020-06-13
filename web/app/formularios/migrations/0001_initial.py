# Generated by Django 3.0.6 on 2020-06-08 23:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoAtencionNecesidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'estados atencion necesidad',
            },
        ),
        migrations.CreateModel(
            name='Necesidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_insercion', models.DateTimeField(verbose_name='fecha insercion')),
                ('descripcion', models.CharField(max_length=300, verbose_name='descripción')),
                ('ayudado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='necesidades', to='base.Persona')),
                ('lugar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='necesidades_ubicadas', to='base.Lugar')),
                ('remitente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='necesidades_ingresadas', to='base.Persona')),
            ],
            options={
                'verbose_name_plural': 'necesidades',
            },
        ),
        migrations.CreateModel(
            name='AtencionNecesidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_ingreso', models.DateTimeField(verbose_name='fecha ingreso')),
                ('fecha_objetivo', models.DateTimeField(verbose_name='fecha objetivo')),
                ('fecha_asignacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha asignacion')),
                ('fecha_finalizacion', models.DateTimeField(blank=True, null=True, verbose_name='fecha finalizacion')),
                ('estado_actual', models.CharField(choices=[('NA', 'No Asignada'), ('A', 'Asignada'), ('F', 'Finalizada')], default='NA', max_length=2)),
                ('necesidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='atenciones', to='formularios.Necesidad')),
            ],
            options={
                'verbose_name_plural': 'atenciones necesidad',
            },
        ),
    ]
