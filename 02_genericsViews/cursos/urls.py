from django.urls import path
from .views import *

urlpatterns = [
    path('cursos/', CursoGenericView.as_view()),
    path('cursos/<str:pk>/', Curso2GenericView.as_view())
]