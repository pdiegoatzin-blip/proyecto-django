from django.shortcuts import render
from .models import Alumnos, ComentarioContacto
from .forms import ComentariosContactoForm
from django.shortcuts import get_object_or_404
import datetime
import datetime
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages
# Create your views here.
def registros(request):
    alumnos=Alumnos.objects.all()
    return render(request, "registros/principal.html",{'alumnos':alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentariosContactoForm(request.POST)
        if form.is_valid(): #Si los datos recibisdos son correctis
            form.save()#inserta
            comentarios=ComentarioContacto.objects.all()
            return render(request, "registros/comentarios.html",
                          {'comentarios':comentarios})
    form = ComentariosContactoForm()
    #si algo sale mal se reenvia al formulario los datos ingresados
    return render(request,'registros/contacto.html',{'form': form})

def contacto(request):
    return render(request,"registros/contacto.html")

def comentarios(request):
    comentarios =  ComentarioContacto.objects.all() 
    return render(request, "registros/comentarios.html", {
        'comentarios': comentarios
    })


def eliminarComentarioContacto(request, id,
        confirmacion='registros/confirmarEliminacion.html'):
        comentario = get_object_or_404(ComentarioContacto, id=id)
        if request.method=='POST':
                comentario.delete()
                comentarios=ComentarioContacto.objects.all()
                return render(request,"registros/comentarios.html",
                                {'comentarios':comentarios})
        return render(request, confirmacion, {'object':comentario})

def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
#get permite establecer una condicionante a la consulta y recupera el objetos
#del modelo que cumple la condición (registro de la tabla ComentariosContacto.
#get se emplea cuando se sabe que solo hay un objeto que coincide con su
#consulta.
    return render(request,"registros/formEditarComentario.html",
{'comentario':comentario})
#Indicamos el lugar donde se renderizará el resultado de esta vista
# y enviamos la lista de alumnos recuparados.

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentariosContactoForm(request.POST, instance=comentario)
#Referenciamos que el elemento del formulario pertenece al comentario
# ya existente
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/comentarios.html",
        {'comentarios':comentarios})
#Si el formulario no es valido nos regresa al formulario para verificar
#datos
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})



def consultar1(request):
    alumnos=Alumnos.objects.filter(carrera='TI')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar2(request):
    alumnos=Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar3(request):
    alumnos=Alumnos.objects.all().only('matricula','nombre','carrera','turno','imagen')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos=Alumnos.objects.filter(turno__contains='Vesp')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos=Alumnos.objects.filter(nombre__in=['Juan',"Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    fechaInicio=datetime.date(2025,10,1)
    fechaFin=datetime.date(2025,12,31)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})






def consultar8(request):
    fechaInicio=datetime.date(2025,11,20)
    fechaFin=datetime.date(2025,11,26)
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito',
    comentario__created__range=(fechaInicio,fechaFin))
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar9(request):
    alumnos=Alumnos.objects.filter(comentario__coment__regex='inscrito')
    return render(request, "registros/consultas.html", {'alumnos': alumnos})


def consultar10(request):
    alumnos=Alumnos.objects.filter(nombre__in=['Ana']) 
    return render(request, "registros/consultas.html", {'alumnos': alumnos})
    

def consultas11(request):
    comentarios = ComentarioContacto.objects.values_list("mensajes", flat=True)
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def consultas12(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__startswith="ola")
    return render(request, "registros/consultas.html", {'comentarios': comentarios})

def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion,
            archivo=archivo)
            insert.save()
            return render(request,"registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request,"registros/archivos.html",{'archivo':Archivos})
    




def consultasSQL(request):
    alumnos = Alumnos.objects.raw(
        'SELECT id, matricula, nombre, carrera, turno, imagen '
        'FROM registros_alumnos '
        'WHERE carrera = "TI" '
        'ORDER BY turno DESC'
    )

    return render(request, "registros/consultas.html", {'alumnos': alumnos})