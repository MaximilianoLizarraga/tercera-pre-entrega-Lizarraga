from django.db import models


class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    editorial = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    
    def __str__(self):
        return f"{self.id} - Titulo: {self.titulo} - Autor: {self.autor} - Editorial: {self.editorial} - Fecha Publicacion: {self.fecha_publicacion}"
    
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad =models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - Nombre: {self.nombre} - Apellido: {self.apellido} - Nacionalidad: {self.nacionalidad} - Fecha de Nacimiento: {self.fecha_nacimiento}"
    
class Genero(models.Model):
    genero = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.id} - {self.genero}"
