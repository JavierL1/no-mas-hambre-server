# Generated by Django 3.0.6 on 2020-06-21 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20200621_1632'),
        ('formularios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, verbose_name='nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Ayuda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, verbose_name='nombre')),
                ('fecha_insercion', models.DateTimeField(verbose_name='fecha de inserción')),
                ('descripcion', models.CharField(max_length=300, verbose_name='descripción')),
                ('rango', models.FloatField(verbose_name='rango')),
                ('activo', models.BooleanField(verbose_name='activo')),
                ('lugar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ayudas', to='base.Lugar', verbose_name='lugar')),
                ('remitente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ayudas', to='base.Participante', verbose_name='remitente')),
                ('tipo_gestion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ayudas', to='base.TipoGestion', verbose_name='tipo de gestión')),
            ],
        ),
        migrations.AddField(
            model_name='proveedor',
            name='fecha_insercion',
            field=models.DateTimeField(default=None, verbose_name='fecha de inserción'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_insercion', models.DateTimeField(verbose_name='fecha de inserción')),
                ('descripcion', models.CharField(max_length=300, verbose_name='descripción')),
                ('remitente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='voluntarios', to='base.Participante', verbose_name='remitente')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='fecha')),
                ('descripcion', models.CharField(max_length=300, verbose_name='descripción')),
                ('accion', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos', to='formularios.Accion', verbose_name='acción')),
                ('ayuda', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos', to='formularios.Ayuda', verbose_name='ayuda')),
                ('lugar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos', to='base.Lugar', verbose_name='lugar')),
                ('necesidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos', to='formularios.Necesidad', verbose_name='necesidad')),
                ('proveedor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos', to='formularios.Proveedor', verbose_name='proveedor')),
                ('voluntario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='eventos', to='formularios.Voluntario', verbose_name='voluntario')),
            ],
        ),
    ]
