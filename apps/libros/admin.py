from django.contrib import admin
from .models import Autor, Libro
# Register your models here.
#para que aparezca en el 8000/admin tengo que colocar acá los modelos que desee
admin.site.register(Autor)
admin.site.register(Libro)
