# Generated by Django 4.2.7 on 2023-12-21 00:54

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('address', models.CharField(max_length=200, verbose_name='Dirección')),
                ('neighborhood', models.CharField(max_length=200, verbose_name='Colonia')),
                ('total', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Total')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('sub_title', models.CharField(max_length=200, verbose_name='Subtítulo')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido')),
                ('cost', models.FloatField(default=150, verbose_name='Costo unitario')),
                ('image', models.ImageField(upload_to='services', verbose_name='Imágen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'ordering': ['created'],
                'permissions': [('can_edit_service', 'Puede hacer todo lo del servicio')],
            },
        ),
    ]
