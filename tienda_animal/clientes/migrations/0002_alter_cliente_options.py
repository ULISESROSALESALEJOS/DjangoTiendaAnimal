# Generated by Django 4.2.2 on 2023-07-01 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'ordering': ['rut']},
        ),
    ]
