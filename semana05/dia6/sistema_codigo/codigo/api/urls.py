from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('alumno',views.AlumnoView.as_view()),
    path('alumno/<int:pk>',views.AlumnoDetailView.as_view()),
    path('curso',views.CursoView.as_view()),
    path('curso/<int:pk>',views.CursoDetailView.as_view()),
    path('evaluacion',views.EvaluacionView.as_view()),
    path('evaluacion/<int:pk>',views.EvaluacionDetailView.as_view()),
]