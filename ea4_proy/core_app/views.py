from django.shortcuts import render, redirect
from core_app.forms import  publicarObra, EditarObra
from core_app.models import Obra
# Create your views here.


def inicio_real(request):
    return render(request, 'core_app/home.html')


def home(request):
    return render(request,'core_app/home.html')

def galeria(request):
    obra = Obra.objects.all()
    datos={
        'obra': obra
    }
    return render(request,'core_app/galeria.html',datos)

#def detalleObra(request, pk):
#    obra = Obra.objects.get(idObra = pk)
#    datos = {
#        'obra': obra
#    }
#    return render(request,'detalleObra.html', datos)

def formulario(request):
    return render(request, 'core_app/formulario.html')
# VISTA QUE SERA USADA EN EL PROYECTO SEMESTRAL
#def registroUsuarios(request):
#    datos={'form': registroUsuario()}
#    if request.method == 'POST':
#        registo_usuario = registroUsuario(request.POST)
#        if registo_usuario.is_valid:
#            registo_usuario.save()
#    return render(request, 'core/registro.html', datos)

def listadoObra(request):
    listado = Obra.objects.all()
    datos = {
        'listado': listado
    }
    return render(request, 'core_app/listadoObras.html', datos)

def add_obra(request):
    datos = {
        'form': publicarObra() 
        }
    if request.method == 'POST':
        formulario_add = publicarObra(request.POST, request.FILES)
        if formulario_add.is_valid:
            formulario_add.save()
            return redirect(to="inicio_home")
    return render(request, 'core_app/crearObra.html', datos)


def edit_obra(request, pk):
    obra = Obra.objects.get(idObra = pk)
    datos = {
        'form': EditarObra(instance= obra) 
        }
    if request.method == 'POST':
        formulario_edit = EditarObra(data=request.POST, instance= obra)
        if formulario_edit.is_valid:
            formulario_edit.save()
            return redirect(to="listado")
    return render(request, 'core_app/editarObra.html', datos)

def borrar_obra(request , pk):
    obra= Obra.objects.get(idObra = pk)
    obra.delete()
    return redirect(to="listado")
    