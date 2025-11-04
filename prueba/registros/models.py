from django.db import models

# Create your models here.
class Alumnos (models.Model):
    matricula = models.CharField(max_length=12,verbose_name="mat")
    nombre = models.TextField()
    carrera = models.TextField()
    turno = models.CharField(max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)



    class Meta:
        verbose_name = 'Alumnos'
        verbose_name_plural = 'Alumnos'
        ordering = ['-created']


    def __str__(self):
        return self.nombre
    #indica que se mostrara el nombre del alumno en el admin


