# Generated by Django 3.2.7 on 2021-10-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_creaciontablafinal'),
    ]

    operations = [
        migrations.AddField(
            model_name='productomodel',
            name='productoEstado',
            field=models.BooleanField(db_column='estado', default=True),
        ),
    ]
