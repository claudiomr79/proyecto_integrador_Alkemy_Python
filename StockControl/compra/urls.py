from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_productos, name='mostrar_productos'),
    path('mostrar_proveedores/', views.mostrar_proveedores, name='mostrar_proveedores'),
    path('crear_producto/',views.crearProducto, name='crear_producto'),
    path('crear_proveedor/', views.crearProveedor, name='crear_proveedor'),
]