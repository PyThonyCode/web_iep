from registro_asistencia import views
from django.urls import path

urlpatterns = [
    path('', views.iniciar_sesion, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # PROFESOR
    path('profesores/', views.profesores, name='lista_profesores'),
    path('profesores/crear', views.agregar_profesor, name='agregar_profesor'),
    path('profesores/<int:id_profesor>/eliminar',
         views.eliminar_profesor, name='eliminar_profesor'),
    path('profesores/<int:id_profesor>/editar',
         views.editar_profesor, name='editar_profesor'),

    # ASISTENCIAS PROFESOR
    path('asistencia_profesor/',
         views.asistencias_profesores, name='lista_asistencias_profesores'),
    path('asistencia_profesor/<int:id_asistencia>',
         views.editar_asistencias_profesores, name='editar_asistencias_profesores'),
    path('asistencia_profesor/crear', views.agregar_asistencia_profesor,
         name='agregar_asistencia_profesor'),
    path('asistencia_profesor/<int:id_asistencia>/eliminar',
         views.eliminar_asistencia_profesor, name='eliminar_asistencia_profesor'),

    # ASISTENCIAS PROFESOR CLASES
    path('asistencia_clase/', views.asistencia_clase,
         name='lista_asistencia_clase'),
    path('asistencia_clase/crear', views.agregar_asistencia_clase,
         name='agregar_asistencia_clase'),
    path('asistencia_claser/<int:id_asistencia>/eliminar',
         views.eliminar_asistencia_clase, name='eliminar_asistencia_clase'),
]
