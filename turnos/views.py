from django.shortcuts import render, redirect
from .forms import TurnosForm
from modelos.models import Turnos
from django.contrib import messages


def turnos_view(request):

    turnos_form = TurnosForm(request.POST or None)

    if request.method == "GET":

        turnos = Turnos.objects.order_by('fecha').values()

        context = {
                    'turnos_form': turnos_form,
                    'turnos'     : turnos
                }

        return render(request, "turnos/turnos.html", context)  

    else:
        if request.method == 'POST':

            if turnos_form.is_valid():

                turnos_form.save()   
                messages.success(request, "Turno guardado con exito")
                
                turnos_form = TurnosForm()

                return redirect('turnos') 

            else:
                
                messages.error(request, "Fecha incorrecta o repetida")
                return redirect('turnos')  


def delete_turnos(request, id):

    Turnos.objects.filter(id=id).delete()

    messages.success(request, "Turno eliminado con exito")

    return redirect('turnos')