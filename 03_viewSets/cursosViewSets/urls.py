from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import *



# utilizando viewSets

router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)

