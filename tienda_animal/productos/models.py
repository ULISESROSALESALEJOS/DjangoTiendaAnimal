from django.db import models

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(db_column='idCategoria', primary_key=True) 
    categoria    = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return str(self.categoria)
    
class Producto(models.Model):
    id_producto      = models.IntegerField(primary_key=True)
    nombre           = models.CharField(max_length=50)
    precio           = models.IntegerField()
    stock            = models.IntegerField()
    descripcion      = models.CharField(max_length=150,blank=False, null=False) 
    id_categoria     = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria')

    def __str__(self):
        return str(self.nombre)
    

#necesito el crud de producto
