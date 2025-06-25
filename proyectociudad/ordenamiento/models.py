from django.db import models

class Parroquia(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ubicacion = models.CharField(max_length=255, choices=[
        ('norte', 'Norte'),
        ('sur', 'Sur'),
        ('este', 'Este'),
        ('oeste', 'Oeste')
    ])
    tipo = models.CharField(max_length=50, choices=[
        ('urbana', 'Urbana'),
        ('rural', 'Rural')
    ])

    def __str__(self):
        return  f"{self.nombre} ({self.tipo}) - {self.ubicacion}"
    
class Barrio(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    num_viviendas = models.PositiveIntegerField()
    num_parques = models.PositiveIntegerField(choices=[
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6')
    ])
    num_edificios = models.PositiveBigIntegerField()
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, related_name='barrios')

    def __str__(self):
        return "%s - %s" % (self.nombre, self.parroquia.nombre)
    