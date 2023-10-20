from django import forms
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
                  'hora_llegada', 'hora_salida', 'motivo_falta']

        widgets = {
            'profesor': forms.Select(attrs={'class': 'form-select', 'style': 'width:400px'}),
            'asistencia': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'fecha_asistencia': forms.DateInput(attrs={'class': 'form-control'}),
            'hora_llegada': forms.TimeInput(attrs={'class': 'form-control'}),
            'hora_salida': forms.TimeInput(attrs={'class': 'form-control'}),
            'motivo_falta': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AsistenciaClaseForm(forms.ModelForm):
    class Meta:
        model = AsistenciaClase
        fields = ['horario', 'profesor', 'area',
                  'sub_area', 'tema', 'grado', 'fecha_asistencia']
        widgets = {
            'horario': forms.Select(attrs={'class': 'form-select'}),
            'profesor': forms.Select(attrs={'class': 'form-select'}),
            'area': forms.Select(attrs={'class': 'form-select'}),
            'sub_area': forms.Select(attrs={'class': 'form-select'}),
            'tema': forms.TextInput(attrs={'class': 'form-control'}),
            'grado': forms.Select(attrs={'class': 'form-select'}),
            'fecha_asistencia': forms.DateInput(attrs={'class': 'form-control'}),
        }
