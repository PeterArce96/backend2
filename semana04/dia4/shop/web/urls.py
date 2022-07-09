from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('',views.index,name='index'),
    path('producto/<int:producto_id>',views.producto,name='producto'),
    path('productosPorCategoria/<int:categoria_id>',views.productosPorCategoria,name='productosPorCategoria'),
    path('carrito',views.carrito,name='carrito'),
    path('login',views.login,name='login')
]