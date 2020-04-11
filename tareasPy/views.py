from django.shortcuts import render
from django.http import HttpResponse
import time

def hello_world(request):
    horaActual = time.strftime("%H:%M:%S")
    horaNoche = time.strftime("20:00:00")
    horaNoche2 = time.strftime("23:59:00")
    horaNoche3 = time.strftime("00:00:00")
    horaNoche4 = time.strftime("05:59:00")
    horaDia = time.strftime("06:00:00")
    horaDia2 = time.strftime("11:59:00")
    mensaje = ""
    if horaActual >= horaNoche and horaActual <= horaNoche2 or (horaActual >= horaNoche3 and horaActual <= horaNoche4):
        mensaje = "Buenas noches..."
    elif horaActual >= horaDia and horaActual <= horaDia2:
        mensaje = "Buenos días..."
    else:
        mensaje = "Buenas tardes..."
    context = {"mensaje":mensaje}
    return render(request, 'home.html', context)
