# Generated by Django 3.0.6 on 2020-06-23 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_auto_20200622_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='alias',
            field=models.CharField(max_length=64, null=True, verbose_name='alias'),
        ),
        migrations.AlterField(
            model_name='region',
            name='posicion',
            field=models.IntegerField(null=True, verbose_name='posición'),
        ),
    ]