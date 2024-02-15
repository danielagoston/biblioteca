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
    fecha_creacion = models.DateField(auto_now = True, auto_now_add = False)

    class Meta:
        #esto se pone para que en el admin aparezcan bien los nombres del modelo
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        #ordenar alfafebicamente
        ordering = ['apellidos', 'nombre']

    #con esta funcion hago que cada objeto creado se llame por su nombre en el admin
    def __str__(self):
        return self.apellidos + ', ' + self.nombre
    

class Libro(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 255, blank = False, null = False)
    fecha_publicacion = models.DateField(blank = False, null = False)
    #auto_now indica la fecha que se modificó o crea automáticamente
    fecha_creacion = models.DateField(auto_now = True, auto_now_add = False)
    '''
    la relación siempre tiene que llevar on_delete (excepto Clave foránea) 
    para que una vez que se borre algú n dato también se borre hacia quién está hecha la relación
     (y si se borra un autor se borra todo)
    '''
    #autor_id = models.OneToOneField(Autor, on_delete = models.CASCADE)
    #autor_id = models.ForeignKey(Autor, on_delete = models.CASCADE)
    autor_id = models.ManyToManyField(Autor)
    
    

    #el class Meta por convención en python es utilizado para definir el comportamiento
    #de otras clases, personalizan el comportamiento de por ejemplo Libro en este caso
    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']

    def __str__(self):
        return self.titulo