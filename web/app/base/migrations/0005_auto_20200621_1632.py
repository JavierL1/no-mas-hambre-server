# Generated by Django 3.0.6 on 2020-06-21 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_tipogestion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizacion',
            options={'verbose_name': 'organización', 'verbose_name_plural': 'organizaciones'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'región', 'verbose_name_plural': 'regiones'},
        ),
        migrations.AlterModelOptions(
            name='tipogestion',
            options={'verbose_name': 'tipo gestión', 'verbose_name_plural': 'tipos gestión'},
        ),
    ]