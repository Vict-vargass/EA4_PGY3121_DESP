from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
import os 

class CategoriaObra(models.Model):
    id_categoria= models.IntegerField(primary_key=True, verbose_name="Id categoria")
    nombreCategoria = models.CharField(max_length=20, verbose_name="Categoria obra")
    
    def __str__(self):
        return self.nombreCategoria



class Obra (models.Model):
    idObra = models.IntegerField(primary_key=True, verbose_name="id solicitud obra")
    nombreObra = models.CharField(max_length=40, verbose_name="nombre obra")
    historia = models.TextField(max_length=3000, verbose_name="historia obra")
    descripcion = models.TextField(max_length=1000, verbose_name="descripcion obra")
    precio= models.CharField(max_length=100, verbose_name="precio obra")
    tecnicaUsada = models.TextField(max_length=1000, verbose_name="tecnica usada obra")
    imagen = models.ImageField(verbose_name="Imagen", null=True, blank=True)
    categoria = models.ForeignKey(CategoriaObra, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreObra
    
    def delete(self, *args, **kwargs ):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(Obra, self).delete(*args, **kwargs)