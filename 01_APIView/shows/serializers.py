from rest_framework import serializers
from .models import *

class BandaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Banda
        fields = '__all__'


class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = '__all__'

class MusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musica
        fields = '__all__'


class IntegranteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Integrante
        fields = '__all__'