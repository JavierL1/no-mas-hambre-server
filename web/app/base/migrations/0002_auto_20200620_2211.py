# Generated by Django 3.0.6 on 2020-06-21 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='dv',
            field=models.IntegerField(default=-1, verbose_name='dv'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='persona',
            name='lugar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='personas', to='base.Lugar'),
        ),
        migrations.AddField(
            model_name='persona',
            name='rut',
            field=models.IntegerField(default=-1, verbose_name='rut'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contacto',
            name='tipo_contacto',
            field=models.CharField(choices=[('NA', 'No Asignada'), ('TM', 'Telefono Movil'), ('TF', 'Telefono Fijo'), ('FB', 'Facebook'), ('TW', 'Twitter'), ('IG', 'Instagram'), ('LI', 'Linked In'), ('EM', 'Email')], default='NA', max_length=2, verbose_name='tipo de contacto'),
        ),
        migrations.DeleteModel(
            name='TipoContacto',
        ),
    ]
