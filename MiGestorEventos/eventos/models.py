from django.db import models

# Create your models here.

class Organizador (models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


class Eventos(models.Model):
    organizador = models.ForeignKey(Organizador, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fecha = models.DateTimeField()
    capacidad = models.PositiveBigIntegerField()
    lugar = models.CharField(max_length=255)
    estado = models.CharField(
        max_length=20,
        choices=[('activo', 'Activo'), ('cancelado', 'Cancelado'), ('finalizado', 'Finalizado')],
        default = 'activo'
    )

    def __str__(self):
        return self.titulo
    



