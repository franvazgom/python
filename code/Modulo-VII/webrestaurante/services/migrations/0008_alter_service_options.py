# Generated by Django 4.2.7 on 2023-11-30 02:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_service_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['created'], 'verbose_name': 'Servicio', 'verbose_name_plural': 'Servicios'},
        ),
    ]
