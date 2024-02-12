from django.db import models

# Create your models here.
#Autor recibe una herencia de models.Model que ya está definido en django
class Autor(models.Model):
    #la primary key es una clave primaria auto incremental / 
    #si no colocamos django la coloca automáticamente
    id = models.AutoField(primary_key = True)
    #en nombre y apellido colocamos Charfield que es un número limitado de caracteres
    #y con blank y null decimos que sea falso a que esté en blanco o sea nulo, es decir es opcional que se escriba algo
    nombre = models.CharField(max_length = 200, blank = False, null = False)
    apellidos = models.CharField(max_length = 200, blank = False, null = False)
    nacionalidad = models.CharField(max_length = 100, blank = False, null = False)
    #textfield es un campo de texto extenso por eso no se aclara cuantos caracteres
    descripcion = models.TextField(blank = False, null = False)  