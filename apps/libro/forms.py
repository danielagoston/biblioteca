from django import forms
from .models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nombre','apellidos','nacionalidad','descripcion']
        labels = {
            'nombre':'Nombres del autor',
            'apellidos':'Apellidos del autor',
            'nacionalidad':'Nacionalidad del autor',
            'descripcion':'Descripción del autor',
        }
        widgets = {
            'nombre':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los nombres del autor',
                    'id':'nombre'
                }
            ),
            'apellidos':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese los apellidos del autor',
                    'id':'apellidos'
                }
            ),
            'nacionalidad':forms.TextInput(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese la nacionalidad del autor',
                    'id':'apellidos'
                }
            ),
            'descripcion':forms.Textarea(
                attrs = {
                    'class':'form-control',
                    'placeholder':'Ingrese una breve descripción',
                    'id':'apellidos'
                }
            ),
        }
