# Generated by Django 3.2.7 on 2021-10-18 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0002_creacion_columna_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productomodel',
            name='productoEstado',
        ),
        migrations.AddField(
            model_name='productomodel',
            name='productoDisponible',
            field=models.BooleanField(db_column='disponible', default=True),
        ),
    ]
