from django.db import models

class Autor(models.Model):
    # cod_autor = models.AutoField(primary_key=True)        
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    # cod_libro = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    año_publicacion = models.IntegerField()
    precio = models.IntegerField()
    imagen = models.TextField()
    descripcion = models.CharField(max_length=2500)
    stock = models.IntegerField()
    firmado = models.BooleanField(default=False)
    hay_envio_gratis = models.BooleanField(default=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

