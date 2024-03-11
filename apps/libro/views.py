from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from .forms import AutorForm
from .models import Autor
from django.views.generic import View


def home(request):
    return render(request, 'index.html')

class Inicio(View):
    pass

def crearAutor(request):
    # Comprueba si la solicitud es de tipo POST.
    if request.method == 'POST':
        # Si la solicitud es POST, crea un formulario de Autor con los datos proporcionados en la solicitud.
        autor_form = AutorForm(request.POST)
        # Comprueba si el formulario es válido.
        if autor_form.is_valid():
            # Si el formulario es válido, guarda los datos del nuevo autor en la base de datos.
            autor_form.save()
            # Redirige al usuario a la página de índice (o cualquier otra página que desees).
            return redirect('libro:listar_autor')
    else:
        # Si la solicitud no es POST, crea un formulario vacío de Autor.
        autor_form = AutorForm()
    
    # Renderiza la plantilla 'libros/crear_autor.html' y pasa el formulario de autor como contexto.
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form})

def listarAutor(request):
    # Recupera todos los autores cuyo estado sea verdadero (activo) desde la base de datos.
    autores = Autor.objects.filter(estado=True)
    
    # Renderiza la plantilla 'listar_autor.html' y pasa la lista de autores recuperados como contexto.
    return render(request, 'libro/listar_autor.html', {'autores': autores})


def editarAutor(request, id):
    # Inicialización de variables
    autor_form = None
    error = None
    try:
        # Intenta obtener el autor de la base de datos usando su ID
        autor = Autor.objects.get(id=id)

        # Si la solicitud es de tipo GET, muestra el formulario con los datos actuales del autor
        if request.method == 'GET':
            autor_form = AutorForm(instance=autor)
        else:
            # Si la solicitud es de tipo POST, procesa el formulario enviado por el usuario
            autor_form = AutorForm(request.POST, instance=autor)
            # Si el formulario es válido, guarda los cambios en la base de datos y redirige al usuario a la página de índice
            if autor_form.is_valid():
                autor_form.save()
                return redirect('index')
    # Maneja la excepción en caso de que el autor no exista
    except ObjectDoesNotExist as e:
        error = e
     
    # Renderiza el template 'libros/crear_autor.html' con el formulario del autor y el mensaje de error (si hay alguno)
    return render(request, 'libro/crear_autor.html', {'autor_form': autor_form,'error':error})

def eliminarAutor(request, id):
    # Obtiene el autor correspondiente al ID proporcionado desde la base de datos.
    autor = Autor.objects.get(id=id)
    
    # Verifica si la solicitud es de tipo POST (es decir, si se ha enviado el formulario de eliminación).
    if request.method == 'POST':
        # Elimina el autor de la base de datos.
        #autor.delete()
        
        # Cambia el estado del autor a Falso.
        autor.estado = False
        # Guarda el cambio en la base de datos.
        autor.save()
        # Redirige al usuario a la vista listar_autor después de "eliminar" el autor.

        # Redirige al usuario a la vista listar_autor después de eliminar el autor.
        return redirect('libro:listar_autor')
    
    # Si la solicitud no es de tipo POST, renderiza la plantilla 'eliminar_autor.html' con los datos del autor.
    return render(request,'libro/eliminar_autor.html',{'autor':autor})
