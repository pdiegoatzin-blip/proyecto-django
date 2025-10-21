from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, HttpResponse

# Create your views here.
menu=""""
    <h1>Menu</h1>
    <ul>
        <li><a href="/principal">Principal</a></li>
        <li><a href="/contacto">Contacto</a></li>
        <li><a href="/registrar">Registrar</a></li>
    </ul>
"""
def principal(request):
    def principal(request):
        return  render(request,"inicio/principal.html")
    # contenido ="<h1>Hola mundo</h1>"
    # return HttpResponse(contenido)

def contacto(request):
    contenido = """
    <h1>Contacto</h1>
    <p> Nombre: <input type="text" name="nombre"></p>
    <p> Mensaje: <textarea name="mensaje"></textarea></p>
    <p> <input type="Button" name="Enviar" value="Enviar"></p>
    """
    return HttpResponse(contenido)

def registrar(request):
    contenido = """
    <h1>Registrar</h1>
    <p> Matricula: <input type="text" name="matricula"></p>
    <p> Nombre: <input type="text" name="nombre"></p>
    <p> Carrera: 
        <select name="carrera">
            <option value="ingenieria">Ingeniería</option>
            <option value="medicina">Medicina</option>
            <option value="derecho">Derecho</option>
        </select>
    </p>
    <p> ¿eliga el turno? 
        <input type="radio" name="turno" value="matutino"> Matutino
        <input type="radio" name="turno" value="vespertino"> Vespertino
    </p>
    """
    return HttpResponse(contenido)