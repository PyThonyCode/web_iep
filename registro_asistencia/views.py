from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from django.db.models import Count
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def dashboard(request):
    # Obtén el conteo de registros en AsistenciaClase y AsistenciaProfesor por fecha
    asistencia_clase_count = AsistenciaClase.objects.values(
        'fecha_asistencia').annotate(total=Count('id'))
    asistencia_profesor_count = AsistenciaProfesor.objects.values(
        'fecha_asistencia').annotate(total=Count('id'))

    return render(request, 'dashboard.html', {
        'asistencia_clase_count': asistencia_clase_count,
        'asistencia_profesor_count': asistencia_profesor_count,
    })
# Administrador inicio sesión


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Usuario creado'
                })
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    'error': 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            'error': 'Contraseña no son iguales'
        })


def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if usuario is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña es incorrecto'
            })
        else:
            login(request, usuario)
            return redirect('dashboard')


@login_required
def cerrar_sesion(request):
    logout(request)
    return redirect('login')


# PROFESORES

@login_required
def profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'profesor/lista.html', {
        'profesores': profesores
    })


@login_required
def agregar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
        else:
            # Si el formulario no es válido, puedes manejarlo aquí, por ejemplo, mostrar errores en el formulario.
            return render(request, 'profesor/agregar.html', {'form': form})
    else:
        return render(request, 'profesor/agregar.html', {'form': ProfesorForm()})


@login_required
def eliminar_profesor(request, id_profesor):
    profesor = get_object_or_404(Profesor, pk=id_profesor)
    if request.method == 'POST':
        profesor.delete()
        return redirect('lista_profesores')
    return render(request, 'profesor/confirmar.html', {'profesor': profesor})


@login_required
def editar_profesor(request, id_profesor):
    profesor = get_object_or_404(Profesor, pk=id_profesor)
    if request.method == 'POST':
        form = ProfesorForm(request.POST, instance=profesor)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
    else:
        form = ProfesorForm(instance=profesor)
    return render(request, 'profesor/editar.html', {'form': form})


# REGISTRO ASISTENCIA PROFESORES
@login_required
def asistencias_profesores(request):
    asistencias = AsistenciaProfesor.objects.all()
    return render(request, 'asistencia_profesor/lista.html', {
        'asistencias': asistencias
    })


@login_required
def editar_asistencias_profesores(request, id_asistencia):
    asistencia = get_object_or_404(AsistenciaProfesor, pk=id_asistencia)
    if request.method == 'POST':
        form = AsistenciaProfesorForm(request.POST, asistencia)
        if form.is_valid():
            form.save()
            return redirect('lista_asistencias_profesores')
    else:
        form = AsistenciaProfesorForm(instance=asistencia)
    return render(request, 'asistencia_profesor/editar.html', {'form': form})


@login_required
def agregar_asistencia_profesor(request):
    if request.method == 'POST':
        form = AsistenciaProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asistencias_profesores')
        else:
            # Si el formulario no es válido, puedes manejarlo aquí, por ejemplo, mostrar errores en el formulario.
            return render(request, 'asistencia_profesor/agregar.html', {'form': form})
    else:
        return render(request, 'asistencia_profesor/agregar.html', {'form': AsistenciaProfesorForm()})


@login_required
def eliminar_asistencia_profesor(request, id_asistencia):
    asistencia = get_object_or_404(AsistenciaProfesor, pk=id_asistencia)
    if request.method == 'POST':
        asistencia.delete()
        return redirect('lista_asistencias_profesores')
    return render(request, 'asistencia_profesor/confirmar.html', {'asistencia': asistencia})


# REGISTRO ASISTENCIA CLASE
@login_required
def asistencia_clase(request):
    asistencias = AsistenciaClase.objects.all()
    return render(request, 'asistencia_clase/lista.html', {
        'asistencias': asistencias
    })


@login_required
def obtener_subareas(request):
    area_id = request.GET.get('area_id')
    sub_areas = SubArea.objects.filter(area_id=area_id).values('id', 'nombre')
    return JsonResponse(list(sub_areas), safe=False)


@login_required
def agregar_asistencia_clase(request):
    if request.method == 'POST':
        form = AsistenciaClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asistencia_clase')
        else:
            # Si el formulario no es válido, puedes manejarlo aquí, por ejemplo, mostrar errores en el formulario.
            return render(request, 'asistencia_clase/agregar.html', {'form': form})
    else:
        return render(request, 'asistencia_clase/agregar.html', {'form': AsistenciaClaseForm()})


@login_required
def eliminar_asistencia_clase(request, id_asistencia):
    asistencia = get_object_or_404(AsistenciaClase, pk=id_asistencia)
    if request.method == 'POST':
        asistencia.delete()
        return redirect('lista_asistencia_clase')
    return render(request, 'asistencia_clase/confirmar.html', {'asistencia': asistencia})
