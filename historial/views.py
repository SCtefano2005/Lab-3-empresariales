from django.shortcuts import render, redirect, get_object_or_404
import uuid 
from django.utils import timezone  # Captura la fecha
from .models import *
from registro.models import Carro

def index_historial(request):
    return render(request, 'index_historial.html')

def registrar_entrada(request):
    if request.method == 'POST':
        placa = request.POST.get('placa')
        try:
            carro = Carro.objects.get(placa=placa)
        except Carro.DoesNotExist:
            return render(request, 'registrar_entrada.html', {'error': 'Placa no registrada'})
        
        codigo = str(uuid.uuid4())[:8]
        visita = Registro_Visita.objects.create(carro=carro, codigo=codigo)
        
        return render(request, 'codigo_ingreso.html', {'codigo': codigo})
    return render(request, 'registrar_entrada.html')

def registrar_salida(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo')
        try:
            visita = Registro_Visita.objects.get(codigo=codigo, fecha_salida__isnull=True)
            visita.fecha_salida = timezone.now()
            visita.save()
            return redirect('salida_exitosa',codigo=visita.codigo)
        except Registro_Visita.DoesNotExist:
            return render(request, 'registrar_salida.html', {'error': 'Código incorrecto o ya ingresado'})
    return render(request, 'registrar_salida.html')

def salida_exitosa(request, codigo):
    visita = get_object_or_404(Registro_Visita, codigo=codigo)
    context = {
        'visita': visita
    }
    return render(request, 'salida_exitosa.html', context)
