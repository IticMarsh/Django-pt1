from .models import Usuari, AssignaturesImpartides
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Usuari
from . import models
from .forms import PersonForm

def student(request):
    students = Usuari.objects.all()
    return render(request, 'student.html', {'students': students})

def teacher(request):
    teachers = Usuari.objects.filter(rol__nom='professor')
    return render(request, 'teacher.html', {'teachers': teachers})

#POST
def user_form(request):
    form = PersonForm()

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    context = {'form':form}
    return render(request, 'form.html', context)



#GET ALL

def index(request):
    persons = Usuari.objects.all()  # Obtener todos los objetos de Usuari
    return render(request, 'student.html', {'data': persons})

#GET BY ID

def indexId(request):

    id_DB = 1
    person = Usuari.objects.get(id = id_DB)
    nom = Usuari.name

#UPDATE
def update_user (request, pk):
    person = Usuari.objects.get(id = pk)
    form = PersonForm(instance=person)

    if request.method == 'POST':
        form = PersonForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('/centre/students')
        
    context = {'form':form}
    return render(request, 'form.html', context)

#DELETE
def delete_user(request, pk):
    person = Usuari.objects.get(id=pk)
    person.delete()
    persons = Usuari.objects.all()  # Obtener todos los objetos de Usuari
    return render(request, 'student.html', {'students': persons})
    
