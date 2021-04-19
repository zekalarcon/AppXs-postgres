from django.shortcuts import render, redirect
from .forms import TrabajosForm, StockForm
from modelos.models import Trabajos, Stock
from django.contrib import messages



def trabajos_view(request):

    trabajo_form = TrabajosForm(request.POST or None)
    stock_form   = StockForm(request.POST or None)

    if request.method == "GET":

        context = {
            "trabajos": trabajo_form,
            "stock": stock_form
        }

        return render(request, "trabajos/trabajos.html", context)

    else:

        if request.method == "POST":    
    
            if trabajo_form.is_valid():

                trabajo_form.save()   
                messages.success(request, "Trabajo creado con exito")
                
                trabajo_form = TrabajosForm()

                return redirect('trabajos')

            elif stock_form.is_valid():

                data = Stock(accion='EGRESO', trabajo_id=Trabajos.objects.latest('id'))
                stock_form = StockForm(request.POST, instance=data)
                stock_form.save()

                nombre = Trabajos.objects.last().nombre  
                messages.success(request, f'Producto agregado con exito a {nombre}')
                
                stock_form = StockForm()
                            
                return redirect('trabajos')

            else:

                messages.error(request, 'Ups algo salio mal, volve a intentar')    

                return redirect('trabajos')