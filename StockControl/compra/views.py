from django.shortcuts import render,redirect
from .models import Producto, Proveedor
from .forms import ProveedorForm, ProductoForm  

def crearProducto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_productos')  
    else:
        form = ProductoForm()
    return render(request, 'crear_producto.html', {'form': form})

def mostrar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def crearProveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mostrar_proveedores')  
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def mostrar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listar_proveedores.html', {'proveedores': proveedores} )

