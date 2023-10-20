from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.utils import timezone

# Modelo para los niveles (Secundaria, Primaria, Inicial)


class Nivel(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para los profesores


class Profesor(models.Model):
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30, blank=True, null=True)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    correo = models.EmailField(max_length=50, unique=True)
    num_dni = models.CharField(max_length=8, unique=True)
    num_celular = models.CharField(max_length=9, unique=True, validators=[
                                   MinLengthValidator(9), MaxLengthValidator(9)])

    def __str__(self):
        return f"{self.apellido_paterno} {self.apellido_materno} {self.primer_nombre}"

# Modelo para los horarios


class Horario(models.Model):
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    def __str__(self):
        return f"{self.hora_inicio} - {self.hora_fin}"

# Modelo para las áreas (Arte y Cultura, Ciencia y Tecnología, ...)


class Area(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre

# Modelo para las sub-áreas (por ejemplo, sub-áreas de Ciencia y Tecnología)


class SubArea(models.Model):
    nombre = models.CharField(max_length=50)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.area.nombre})"

# Modelo para los temas


# class Tema(models.Model):
#    nombre = models.CharField(max_length=50)
#    area = models.ForeignKey(Area, on_delete=models.CASCADE)
#
#    def __str__(self):
#        return f"{self.nombre} ({self.area.nombre})"

# Modelo para los grados


class Grado(models.Model):
    nombre = models.CharField(max_length=50)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} ({self.nivel.nombre})"

# Modelo para la asistencia del profesor al colegio


class AsistenciaProfesor(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    asistencia = models.BooleanField()
    fecha_asistencia = models.DateField(default=timezone.now)
    hora_llegada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)
    motivo_falta = models.TextField(blank=True)

    def __str__(self):
        return f"Asistencia de {self.profesor} el {self.fecha_asistencia}"

# Modelo para la asistencia a clase


class AsistenciaClase(models.Model):
    horario = models.ForeignKey(Horario, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    sub_area = models.ForeignKey(SubArea, on_delete=models.CASCADE)
    tema = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    fecha_asistencia = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Asistencia de {self.profesor} a {self.area.nombre} - {self.grado.nombre} el {self.fecha_asistencia}"
