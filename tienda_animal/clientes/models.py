from django.db import models

# Create your models here.
class Genero(models.Model):
    id_genero  = models.AutoField(db_column='idGenero', primary_key=True) 
    genero     = models.CharField(max_length=20, blank=False, null=True)

    def __str__(self):
        return str(self.genero)

class Cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=True) 
    id_genero        = models.ForeignKey('Genero',on_delete=models.CASCADE, db_column='idGenero')  
    telefono         = models.CharField(max_length=45)
    direccion        = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)
    
    class Meta:
        ordering = ['rut']

    class Contacto(models.Model):
        correo      = models.EmailField()
        nombre      = models.CharField(max_length=50)
        apellido    = models.CharField(max_length=50)
        telefono    = models.TextField()
        ciudad      = models.CharField(max_length=50)
        residencia  = models.CharField(max_length=50)
