from django import forms
from django.utils import timezone
from .models import *


class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['primer_nombre', 'segundo_nombre', 'apellido_paterno',
                  'apellido_materno', 'correo', 'num_dni', 'num_celular']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control', 'style': "border-radius: 0.8rem ;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);"}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control', 'style': "border-radius: 0.8rem ;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);"}),
            'apellido_paterno': forms.TextInput(attrs={'class': 'form-control', 'style': "border-radius: 0.8rem ;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);"}),
            'apellido_materno': forms.TextInput(attrs={'class': 'form-control', 'style': "border-radius: 0.8rem ;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);"}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'style': "border-radius: 0.8rem ;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);"}),
            'num_dni': forms.TextInput(attrs={'class': 'form-control', 'style': "border-radius: 0.8rem ;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);"}),
            'num_celular': forms.TextInput(attrs={'class': 'form-control', 'style': "border-radius: 0.8rem ;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);"}),
        }


class AsistenciaProfesorForm(forms.ModelForm):
    class Meta:
        model = AsistenciaProfesor
        fields = ['profesor', 'asistencia', 'fecha_asistencia',
                  'hora_llegada', 'hora_salida']

        widgets = {
            'profesor': forms.Select(attrs={'class': 'form-select', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'asistencia': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'width:20px; height:20px;border-color:rgb(174, 94, 129,0.8);'}),
            'fecha_asistencia': forms.DateInput(attrs={'class': 'form-control', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'hora_llegada': forms.TimeInput(attrs={'class': 'form-control',  'placeholder': "06:00:00", 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'hora_salida': forms.TimeInput(attrs={'placeholder': "13:30:00", 'class': 'form-control', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
        }


class AsistenciaClaseForm(forms.ModelForm):
    class Meta:
        model = AsistenciaClase
        fields = ['horario', 'profesor', 'area',
                  'sub_area', 'tema', 'grado', 'fecha_asistencia']
        widgets = {
            'horario': forms.Select(attrs={'class': 'form-select', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'profesor': forms.Select(attrs={'class': 'form-select', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'area': forms.Select(attrs={'class': 'form-select', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'sub_area': forms.Select(attrs={'class': 'form-select', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'tema': forms.TextInput(attrs={'class': 'form-control', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'grado': forms.Select(attrs={'class': 'form-select', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
            'fecha_asistencia': forms.DateInput(attrs={'class': 'form-control', 'style': 'width:400px;background-color: rgba(243, 238, 81, 0.411);border-color:rgb(174, 94, 129,0.8); font-size: 18px; box-shadow: 2px 2px 5px rgba(174, 94, 129, 0.712);'}),
        }
