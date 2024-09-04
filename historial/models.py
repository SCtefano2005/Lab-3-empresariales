from django.db import models
from registro.models import Carro

class Registro_Visita(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE, related_name="visitas")
    codigo = models.CharField(max_length=100, unique=True, verbose_name="Codigo de ingreso")
    fecha_entrada = models.DateTimeField(auto_now_add= True, verbose_name="Hora de entrada")
    fecha_salida = models.DateTimeField(null=True, blank=True, verbose_name="Hora de salida")
    
    def __str__(self):
        return f"{self.carro.placa} - {self.fecha_entrada} - {self.codigo}"