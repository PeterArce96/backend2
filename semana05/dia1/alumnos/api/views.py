from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'mensaje':'Bienvenido a mi API con Django'
    }
    return JsonResponse(context)