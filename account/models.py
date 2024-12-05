from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    pass

# Create your models here.

class Perfil(models.Model):
    GENERO_CHOICES = [
        ("M", "Masculino"),
        ("F", "Femenino"),
        ("O", "Otro"),
    ]
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE
    )
    profesion = models.CharField(max_length=100, default="debes agregar una profesion")
    puesto_actual = models.CharField(
        max_length=100, default="debes agregar un puesto actual"
    )
    empresa = models.CharField(max_length=100, default="debes agregar una empresa")
    telefono = models.CharField(max_length=50, default="debes agregar un telefono")
    direccion = models.CharField(max_length=100, default="debes agregar una direccion")
    ciudad = models.CharField(max_length=100, default="debes agregar una ciudad")
    estado = models.CharField(max_length=100, default="debes agregar un estado")
    pais = models.CharField(max_length=100, default="debes agregar un pais")
    codigo_postal = models.CharField(max_length=5, default="codigo postal")
    fecha_nacimiento = models.DateField(default="2021-01-01")
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES, default="O")
    foto = models.ImageField(upload_to="avatar", null=True, blank=True)
    curriculum = models.FileField(upload_to="curriculums/", null=True, blank=True)

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        db_table = "perfil"

    def __str__(self):
        return self.empresa
