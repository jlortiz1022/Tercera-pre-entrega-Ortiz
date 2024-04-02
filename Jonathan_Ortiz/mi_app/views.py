from django.shortcuts import render
from mi_app.models import Curso
from mi_app.models import Profesor
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def inicio(request):
    return render(request , "padre.html")




def alta_curso(request,nombre):
    curso=Curso(nombre=nombre , camada=2436) 
    curso.save()
    texto=f"se guardo en la bd el curso: {curso.nombre} {curso.camada}"
    return HttpResponse(texto)

def ver_cursos(request):
    cursos=Curso.objects.all() #trae toda la lista de curso
    dicc={"cursos": cursos}
    plantilla=loader.get_template("cursos.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

def alumnos(request):
    return render(request,"alumnos.html")

def alta_profesor(request,nombre):
    profesor=Profesor(nombre=nombre,camada=2436) 
    profesor.save()
    texto=f"se guardo en la bd el profesor: {profesor.nombre} {profesor.camada}"
    return HttpResponse(texto)

def ver_profesores(request):
    profesores=Profesor.objects.all() #trae toda la lista de curso
    dicc={"profesores": profesores}
    plantilla=loader.get_template("profesores.html")
    documento=plantilla.render(dicc)
    return HttpResponse(documento)

    



    
