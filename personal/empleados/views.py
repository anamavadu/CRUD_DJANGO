from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Empleado

# Create your views here.

def holaMundo(request):
    return HttpResponse("Hola Mundo ADSO")

def inicio(request):
    return render(request, 'inicio.html')

def lista_empleados(request):
    empleados_list = Empleado.objects.all()
    return render(request, 'empleados.html', {'empleados': empleados_list})

def detalle(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'detalle.html', {'empleado': empleado})