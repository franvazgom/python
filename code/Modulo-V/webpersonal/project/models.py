from django.db import models

class Project(models.Model):
    title       = models.CharField(max_length=100, verbose_name='Título del proyecto')
    description = models.TextField(verbose_name='Descripción')
    image       = models.ImageField(verbose_name='Imágen', upload_to='project')
    link        = models.URLField(null=True, blank=True, verbose_name='Liga')
    
    #Se guarda la fecha cuando se crea
    created     = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')   
    #Se guarda la fecha cuando se crea y cuando se modifica
    updated     = models.DateTimeField(auto_now =True, verbose_name='Fecha de modificación')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'

        #Se van a ordenar del mas nuevo al mas viejo
        ordering = ['-created']

    def __str__(self):
        return self.title
