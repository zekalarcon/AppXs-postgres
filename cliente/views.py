from django.shortcuts import render, redirect
from .forms import ClienteForm
from modelos.models import Trabajos, Stock
from collections import defaultdict
from django.contrib import messages


def cliente_view(request):
    
    cliente_form = ClienteForm(request.POST or None)

    if request.method == "GET":

        context = {
                "cliente": cliente_form,   
                }

        return render(request, "cliente/cliente.html", context)
    
    else:
        if request.method == "POST":
            if cliente_form.is_valid():

                trabajos = Trabajos.objects.filter(nombre=cliente_form.cleaned_data['nombre'].upper()).order_by('-fecha').values().all()
                
                
                if trabajos:

                    dic = defaultdict(dict)

                    for data in trabajos:
                        productos = Stock.objects.filter(trabajo_id=data['id']).values().all()
                        
                        
                        for i in productos:

                            producto = i['producto']
                            cantidad = i['cantidad']
                            
                            dic[i['trabajo_id_id']][producto] = cantidad
                        
                    
                    dic_items = dic.items()
                    
                    cliente_form = ClienteForm()
                   
                    context = {
                        "cliente"   : cliente_form,
                        "trabajos"  : trabajos,
                        "productos" : dic_items,
                        'dic'       : dic
                    }    

                    return render(request, "cliente/cliente.html", context)

                else:
                    
                    messages.error(request, "Cliente no existe")
                    return redirect('cliente')
                   
                    
def delete_cliente(request, id):

    Trabajos.objects.filter(id=id).delete()

    messages.success(request, "Cliente eliminado con exito")

    return redirect('cliente')