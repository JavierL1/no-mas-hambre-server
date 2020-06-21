# Generated by Django 3.0.6 on 2020-06-21 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20200620_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64, verbose_name='nombre')),
                ('apellido', models.CharField(blank=True, max_length=64, null=True, verbose_name='apellido')),
                ('rut', models.IntegerField(blank=True, null=True, verbose_name='rut')),
                ('dv', models.IntegerField(blank=True, null=True, verbose_name='dv')),
            ],
        ),
        migrations.AlterField(
            model_name='comuna',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comunas', to='base.Region', verbose_name='comuna'),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactos', to='base.Persona', verbose_name='persona'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='comuna',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lugares', to='base.Comuna', verbose_name='comuna'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='apellido',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='apellido'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='dv',
            field=models.IntegerField(blank=True, null=True, verbose_name='dígito verificador'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='lugar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personas', to='base.Lugar', verbose_name='lugar'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='rut',
            field=models.IntegerField(blank=True, null=True, verbose_name='rut'),
        ),
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True, verbose_name='activo')),
                ('organizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='org_participantes', to='base.Organizacion', verbose_name='persona')),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='per_participantes', to='base.Persona', verbose_name='persona')),
            ],
        ),
        migrations.AddField(
            model_name='organizacion',
            name='lugar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizaciones', to='base.Lugar', verbose_name='lugar'),
        ),
    ]