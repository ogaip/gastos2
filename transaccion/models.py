from django.db import models
from account.models import Perfil

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"

    def __str__(self):
        return self.nombre

class Transaccion(models.Model):
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_transaccion = models.CharField(max_length=10, choices=[('income', 'Ingreso'), ('expense', 'Gasto')])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    fecha_transaccion = models.DateField()
    modificado_en = models.DateTimeField(auto_now=True)
    creado_en = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Transaccion"
        verbose_name_plural = "Transacciones"
        db_table = "transaccion"

    def __str__(self):
        return f"{self.tipo_transaccion} - {self.monto} - {self.fecha_transaccion} - {self.perfil.user.username}"    

