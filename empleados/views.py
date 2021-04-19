from django.shortcuts import render, redirect
from .forms import EmpleadosForm, EmpleadosInfoForm
from modelos.models import Empleados, Trabajos
from django.contrib import messages
import datetime


def empleados_view(request):

    empleados_form = EmpleadosForm(request.POST or None)
    info_form = EmpleadosInfoForm(request.POST or None)

    if request.method == 'GET':

        empleados = Empleados.objects.order_by('fecha').values()

        context = {
                    'empleados_form':empleados_form,
                    'empleados'     :empleados,
                    'info_form'     :info_form
                  }

        return render(request, 'empleados/empleados.html', context)

    else:

        if request.method == 'POST':

            if empleados_form.is_valid():

                empleados_form.save()   
                messages.success(request, "Empleado creado con exito")
                
                empleados_form = EmpleadosForm()

                return redirect('empleados')  

            
                
            elif info_form.is_valid():
            
                nombre = info_form.cleaned_data['nombre_consulta'].upper()
                inicio = info_form.cleaned_data['fecha_inicio'] - datetime.timedelta(days=1)
                fin    = info_form.cleaned_data['fecha_fin'] + datetime.timedelta(days=1)

                lista_trabajos = []
                items_empleado = []

                empleados = Empleados.objects.order_by('fecha').values()
                trabajos = Trabajos.objects.filter(empleado=nombre).filter(fecha__gte=inicio, fecha__lte=fin ).values()
                
                total = sum([x['precio'] for x in trabajos])

                for item in trabajos:

                    if item['trabajo'] not in lista_trabajos:

                        lista_trabajos.append(item['trabajo'])      

                for trabajo in lista_trabajos:

                    cantidad = trabajos.filter(trabajo=trabajo).count()
                    trabajos_filtrados = trabajos.filter(trabajo=trabajo).values()

                    suma_precios = sum([x['precio'] for x in trabajos_filtrados])

                    items_empleado.append([trabajo, cantidad, suma_precios]) 

                empleados_form = EmpleadosForm()
                info_form = EmpleadosInfoForm()

                context = {
                            'empleados_form':empleados_form,
                            'empleados'     :empleados,
                            'info_form'     :info_form,
                            'items_empleado':items_empleado,
                            'total'         :total,
                            }  

                return render(request, 'empleados/empleados.html', context)

            else:

                messages.error(request, "Fecha incorrecta")
                
                return redirect('empleados')


def delete_empleados(request, id):

    Empleados.objects.filter(id=id).delete()

    messages.success(request, "Empleado eliminado con exito")

    return redirect('empleados')                  
