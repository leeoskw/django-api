from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
# Create your views here.



class BandaAPIView(APIView):
    def get(self, request):
        bandas = Banda.objects.all()
        serializer = BandaSerializer(bandas, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BandaSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GeneroAPIView(APIView):
    def get(self, request):
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = GeneroSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class MusicaAPIView(APIView):
    def get(self, request):
        musicas = Musica.objects.all()
        serializer = MusicaSerializer(musicas, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)


    def post(self, request):
        serializer = MusicaSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class IntegranteAPIView(APIView):
    def get(self, request):
        integrantes = Integrante.objects.all()
        serializer = IntegranteSerializer(integrantes, many = True)
        return Response(serializer.data, status = status.HTTP_200_OK)
    

    def post(self, request):
        serializer = IntegranteSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
