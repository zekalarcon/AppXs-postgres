from django.shortcuts import render, redirect
from .forms import AgregarStockForm, ConsultaStockForm
from modelos.models import Stock
from django.contrib import messages


def stock_view(request):

    agregar_form   = AgregarStockForm(request.POST or None)
    consulta_form  = ConsultaStockForm(request.POST or None)

    if request.method == "GET":

        stock_ingreso = Stock.objects.filter(accion='INGRESO').values().all()
        stock_egreso  = Stock.objects.filter(accion='EGRESO').values().all()

        stock = {}

        for i in stock_ingreso:

            producto = i['producto']
            cantidad = i['cantidad']

            if (producto in stock) == False:

                stock[producto] = 0

            stock[producto] = stock[producto]  + cantidad   

        for x in stock_egreso:

            producto = x['producto']
            cantidad = x['cantidad']

            if (producto in stock) == False:

                stock[producto] = 0

            stock[producto] = stock[producto]  - cantidad
            
        sorted_dict = dict(sorted(stock.items()))
        stock_items = sorted_dict.items()    

        context = {
                    "agregar" : agregar_form,
                    "consulta": consulta_form,
                    "stock"   : stock_items
                }

        return render(request, "stock/stock.html", context)
            
    else:

        if request.method == "POST":

            if agregar_form.is_valid():

                data = Stock(accion='INGRESO', trabajo_id=None)
                agregar_form = AgregarStockForm(request.POST, instance=data)
                agregar_form.save()

                messages.success(request, f'Producto agregado con exito aL STOCK')

                agregar_form  = AgregarStockForm()
                consulta_form = ConsultaStockForm()

                context = {
                            "agregar" : agregar_form,
                            "consulta": consulta_form
                        }

                return redirect('stock')

            else:

                if consulta_form.is_valid():

                    producto = consulta_form.cleaned_data['producto_consulta'].upper()

                    stock_ingreso = Stock.objects.filter(producto=producto).filter(accion='INGRESO').values().all()
                    stock_egreso  = Stock.objects.filter(producto=producto).filter(accion='EGRESO').values().all()

                    suma_ingreso = sum([x['cantidad'] for x in stock_ingreso])
                    suma_egreso  = sum([x['cantidad'] for x in stock_egreso])

                    total = suma_ingreso - suma_egreso
                    
                    agregar_form  = AgregarStockForm()
                    consulta_form = ConsultaStockForm()

                    context = {
                                "agregar" : agregar_form,
                                "consulta": consulta_form,
                                "cantidad": total,
                                "producto": producto
                    }

                    return render(request, "stock/stock.html", context)
                    

def delete_stock(request, producto):
    Stock.objects.filter(producto=producto).filter(accion='INGRESO').all().delete()

    messages.success(request, f"{producto} eliminado con exito del STOCK")

    return redirect('stock')