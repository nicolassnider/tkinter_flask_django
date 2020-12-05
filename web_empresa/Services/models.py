from django.db import models

# Create your models here.
class service(models.Model):
    """
    docstring
    """
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.CharField(max_length=200, verbose_name="Subtitulo")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen",upload_to="services")
    link = models.URLField(null=True, blank=True, verbose_name="Link")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class meta():
        """
        docstring
        """
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        ordering = ['-created']

    def __str__(self):
        return self.title