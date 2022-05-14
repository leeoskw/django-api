from rest_framework import generics
from .models import *
from .serializers import *

# get (todos elementos) e POST em um novo elemento -> através do ListCreate

class CursoGenericView(generics.ListCreateAPIView): 
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoGenericView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerialiazer



# filtrando por um ID e DELETE -> através do RetrieveUpdateDestroy

class Avaliacao2GenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerialiazer


class Curso2GenericView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
