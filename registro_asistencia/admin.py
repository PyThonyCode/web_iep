from django.contrib import admin
from .models import Profesor, Horario, Area, Nivel, SubArea, Grado, AsistenciaProfesor, AsistenciaClase

# Register your models here.


class ProfesorAdmin(admin.ModelAdmin):
  list_display = (primer_nombre, apellido_paterno, apellido_materno, num_dni, num_celular)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(Nivel)
admin.site.register(Grado)
admin.site.register(Horario)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(AsistenciaProfesor)
admin.site.register(AsistenciaClase)
