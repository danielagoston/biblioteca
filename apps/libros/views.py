from django.shortcuts import render, redirect
from .forms import AutorForm
from .models import Autor


def Home(request):
    return render(request, 'index.html')

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
            return redirect('index')
    else:
        # Si la solicitud no es POST, crea un formulario vacío de Autor.
        autor_form = AutorForm()
    
    # Renderiza la plantilla 'libros/crear_autor.html' y pasa el formulario de autor como contexto.
    return render(request, 'libros/crear_autor.html', {'autor_form': autor_form})

def listarAutor(request):
    # Obtiene todos los objetos Autor de la base de datos.
    autores = Autor.objects.all()
    
    # Renderiza la plantilla 'libros/listar_autor.html' y pasa la lista de autores como contexto.
    return render(request, 'libros/listar_autor.html', {'autores': autores})


def editarAutor(request, id):
    # Obtiene el objeto Autor correspondiente al ID proporcionado en la URL.
    autor = Autor.objects.get(id=id)
    
    # Comprueba si la solicitud es de tipo GET.
    if request.method == 'GET':
        # Si la solicitud es GET, crea un formulario de Autor con los datos del autor obtenido.
        autor_form = AutorForm(instance=autor)
    else:
        # Si la solicitud no es GET (probablemente POST), crea un formulario de Autor con los datos proporcionados en la solicitud.
        autor_form = AutorForm(request.POST, instance=autor)
        # Comprueba si el formulario es válido.
        if autor_form.is_valid():
            # Si el formulario es válido, guarda los cambios en el objeto Autor.
            autor_form.save()
            # Redirige al usuario a la página de índice (o cualquier otra página que desees).
            return redirect('index')
    
    # Renderiza la plantilla 'libros/crear_autor.html' y pasa el formulario de autor como contexto.
    return render(request, 'libros/crear_autor.html', {'autor_form': autor_form})

