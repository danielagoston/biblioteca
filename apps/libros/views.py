from django.shortcuts import render, redirect
from .forms import AutorForm


def Home(request):
    return render(request, 'index.html')

def crearAutor (request):
    #Si el usuario envía los datos, valido el POST con protocolo HTTP y si es correcto lo guardo
    if request.method == 'POST':
        #creo una variable y tome el form y tome los datos con mi request
        autor_form = AutorForm(request.POST)
        #si estos datos son correctos los guardo en mi BD
        if autor_form.is_valid():
            autor_form.save()
            return redirect('index')
    else:
        #si no está creado, traigo el formulario en blanco para que lo vea el usuario
        autor_form = AutorForm()
    return render(request,'libros/crear_autor.html', {'autor_form':autor_form})
