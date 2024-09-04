from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombres")
    lastname = models.CharField(max_length=200, verbose_name="Apellidos")
    email = models.EmailField(max_length=200, unique=True, verbose_name="Correo Electrónico")
    dni = models.CharField(max_length=8, unique=True, verbose_name="DNI")
    telefono = models.CharField(max_length=9, verbose_name="Numero telefonico")
    flat_number = models.CharField(max_length=50, verbose_name="Numero de departamento")
    

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return f"{self.name} {self.lastname} {self.flat_number} {self.email} {self.telefono}"
    
class Tipo_V(models.Model):
    tipo = models.CharField(max_length=80, verbose_name="Tipo de Vehículo")
    
    class Meta:
        verbose_name = "Tipo de Vehículo"
        verbose_name_plural = "Tipos de Vehículos"
    
    def __str__(self):
        return self.tipo

class Carro(models.Model):
    placa = models.CharField(max_length=10, unique=True, verbose_name="Placa")
    tipo = models.ForeignKey(Tipo_V, on_delete=models.CASCADE, related_name="carros")
    marca = models.CharField(max_length=100, verbose_name="Marca del vehiculo")
    modelo = models.CharField(max_length=150, verbose_name="Modelo del vehiculo")
    color = models.CharField(max_length=90, verbose_name="Color del Vehiculo")
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="carros")
    
    class Meta: 
        verbose_name = "Carro"
        verbose_name_plural = "Carros"
        
    def __str__(self):
        return f"{self.placa} ({self.tipo.tipo}) {self.marca} {self.modelo} {self.color}"
