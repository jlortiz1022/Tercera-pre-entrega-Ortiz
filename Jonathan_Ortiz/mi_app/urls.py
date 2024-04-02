from django.urls import path
from . import views
urlpatterns = [
    path("", views.inicio,name="home"),
    path("alta_curso/<nombre>", views.alta_curso),
    path("ver_cursos",views.ver_cursos, name="cursos"),
    path("alumnos", views.alumnos,name="alumnos"),
    path("alta_profesor/<nombre>",views.alta_profesor),
    path("ver_profesores",views.ver_profesores, name="profesores"),
    
]
