# Generated by Django 4.1.4 on 2023-06-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['rut']},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='genero',
            name='genero',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
