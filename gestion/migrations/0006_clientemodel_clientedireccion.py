# Generated by Django 3.2.7 on 2021-10-30 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_alter_adopcionmodel_adopciontamanio'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientemodel',
            name='clienteDireccion',
            field=models.CharField(db_column='direccion', max_length=50, null=True, verbose_name='Dirección del usuario'),
        ),
    ]
