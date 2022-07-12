import imp
from multiprocessing.spawn import import_main_path
from django.contrib import admin

# Register your models here.
from .models import Alumno

admin.site.register(Alumno)