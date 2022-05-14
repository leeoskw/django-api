from rest_framework import viewsets

from .models import *
from .serializers import *

# utilizando ViewSets para substituir APIViews 

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerialiazer
