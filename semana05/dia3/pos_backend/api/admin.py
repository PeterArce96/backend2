from django.contrib import admin

# Register your models here.
from .models import Categoria, Mesa, Plato,Pedido,PedidoPlato

admin.site.register(Mesa)
admin.site.register(Categoria)
admin.site.register(Plato)
admin.site.register(Pedido)
admin.site.register(PedidoPlato)
