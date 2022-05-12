from django.urls import path
from .views import *

urlpatterns = [
    path('bandas/', BandaAPIView.as_view(), name='bandas'),
    path('generos/', GeneroAPIView.as_view(), name='generos'),
    path('musicas/', MusicaAPIView.as_view(), name='musicas'),


]