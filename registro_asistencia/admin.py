from django.contrib import admin
from .models import Profesor, Horario, Area, Nivel, SubArea, Grado, AsistenciaProfesor, AsistenciaClase

# Register your models here.

admin.site.register(Profesor)
admin.site.register(Nivel)
admin.site.register(Grado)
admin.site.register(Horario)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(AsistenciaProfesor)
admin.site.register(AsistenciaClase)
