"""AppXs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from trabajos.views import trabajos_view
from cliente.views import cliente_view, delete_cliente
from registro.views import login_view, logout_view
from stock.views import stock_view, delete_stock
from turnos.views import turnos_view, delete_turnos
from resumen.views import resumen_view
from empleados.views import empleados_view, delete_empleados

urlpatterns = [
    path('', login_view, name='login'),
    path('trabajos/', trabajos_view, name='trabajos'),
    path('cliente/', cliente_view, name='cliente'),
    path('deletecliente/<int:id>/', delete_cliente, name='delete_cliente'),
    path('turnos/', turnos_view, name='turnos'),
    path('deleteturno/<int:id>/', delete_turnos, name='delete_turno'),
    path('stock/', stock_view, name='stock'),
    path('delete/<str:producto>/', delete_stock, name='delete_stock'),
    path('empleados/', empleados_view, name='empleados'),
    path('deleteempleados/<int:id>/', delete_empleados, name='delete_empleados'),
    path('resumen/', resumen_view, name='resumen'),
    path('logout/', logout_view, name='logout'),
    path('desarrollador/', admin.site.urls),
]
