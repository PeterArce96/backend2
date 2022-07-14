from django.contrib import admin

# Register your models here.
from .models import Categoria, Mesa

admin.site.register(Mesa)
admin.site.register(Categoria)
