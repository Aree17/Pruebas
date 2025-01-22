from django.shortcuts import render
from django.shortcuts import render
from .models import Factura, Mesero, Mesa, Producto, Item_Factura
from django.db.models import Count, Sum
from datetime import date
from .models import  Item_Factura
def estadistica(request):
    return render(request, 'estadisticas/estadistica.html')


def estadisticas_meseros(request):
    fecha_inicio = request.GET.get('fecha_inicio', date.today())
    fecha_fin = request.GET.get('fecha_fin', date.today())

    # Obtener datos de meseros
    facturas = Factura.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
    meseros = (
        facturas.values('mesero__nombre')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    return render(request, 'estadisticas/meseros.html', {
        'meseros': meseros,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })

# Estadísticas de Mesas
def estadisticas_mesas(request):
    fecha_inicio = request.GET.get('fecha_inicio', date.today())
    fecha_fin = request.GET.get('fecha_fin', date.today())

    # Obtener datos de mesas
    facturas = Factura.objects.filter(fecha__range=[fecha_inicio, fecha_fin])
    mesas = (
        facturas.values('mesa__codigo')
        .annotate(total=Count('id'))
        .order_by('-total')
    )

    return render(request, 'estadisticas/mesas.html', {
        'mesas': mesas,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })

# Estadísticas de Productos
def estadisticas_productos(request):
    fecha_inicio = request.GET.get('fecha_inicio', date.today())
    fecha_fin = request.GET.get('fecha_fin', date.today())

    # Obtener datos de productos
    item_facturas = Item_Factura.objects.filter(factura__fecha__range=[fecha_inicio, fecha_fin])
    productos = (
        item_facturas.values('producto__nombre')
        .annotate(total_vendido=Sum('cantidad'))
        .order_by('-total_vendido')
    )

    return render(request, 'estadisticas/productos.html', {
        'productos': productos,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
    })
