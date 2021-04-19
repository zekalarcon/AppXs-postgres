from django.shortcuts import render, redirect
from .forms import ResumenForm
from modelos.models import Trabajos
from django.contrib import messages
import datetime

def resumen_view(request):

    resumen_form = ResumenForm(request.POST or None)

    if request.method == 'GET':

        context = {
                    'resumen_form':resumen_form
                  }

        return render(request, "resumen/resumen.html", context )

    else:

        if request.method == 'POST':

            if resumen_form.is_valid():

                inicio = resumen_form.cleaned_data['fecha_inicio'] - datetime.timedelta(days=1)
                fin    = resumen_form.cleaned_data['fecha_fin'] + datetime.timedelta(days=1)

                tarjeta  = Trabajos.objects.filter(fecha__gte=inicio, fecha__lte=fin ).filter(tarjeta=True).values()
                efectivo = Trabajos.objects.filter(fecha__gte=inicio, fecha__lte=fin ).filter(tarjeta=False).values()
                
                suma_tarjeta  = sum([x['precio'] for x in tarjeta])
                suma_efectivo = sum([x['precio'] for x in efectivo])

                total = suma_tarjeta + suma_efectivo

                resumen_form = ResumenForm()

                context = {
                            'resumen_form'  : resumen_form,
                            'total_efectivo': suma_efectivo,
                            'total_tarjeta' : suma_tarjeta,
                            'total'         : total
                }
                
                return render(request, "resumen/resumen.html", context )

            else:

                messages.error(request, 'Fecha incorrecta')
                
                return redirect('resumen')       