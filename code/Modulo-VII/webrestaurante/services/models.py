from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Order(models.Model):
    email   = models.EmailField(verbose_name='Email')
    name    = models.CharField(max_length=100, verbose_name='Nombre')
    address = models.CharField(max_length=200, verbose_name='Dirección')
    neighborhood  = models.CharField(max_length=200, verbose_name='Colonia')
    total   = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Total')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-created']
    
    def __str__(self):
        return self.emails

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')    
    sub_title = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = RichTextUploadingField(verbose_name='Contenido')
    cost = models.FloatField(verbose_name='Costo unitario', default=150)
    quantity = models.IntegerField(verbose_name='Cantidad', default=5)
    image = models.ImageField(upload_to='services', verbose_name='Imágen') 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['created']
        permissions = [
            ('can_edit_service','Puede hacer todo lo del servicio'),
        ]
    
    def __str__(self):
        return self.title