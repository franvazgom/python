from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Título')    
    sub_title = models.CharField(max_length=200, verbose_name='Subtítulo')
    content = RichTextUploadingField(verbose_name='Contenido')
    image = models.ImageField(upload_to='services', verbose_name='Imágen') 
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'
        ordering = ['-updated']
    
    def __str__(self):
        return self.title