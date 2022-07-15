from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view()),
    path('categoria',views.CategoriaView.as_view()),
    path('mesa',views.MesaView.as_view()),
    path('plato',views.PlatoView.as_view()),
    path('categoria/<int:categoria_id>/',views.CategoriaDetail.as_view()),
    path('categoria/<int:categoria_id>/platos',views.CategoriaPlatosView.as_view())
]
