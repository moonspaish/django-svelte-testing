from django.shortcuts import render
from rest_framework import generics
from films.models import Film
from films.serializers import FilmSerializer
from rest_framework import viewsets
# Create your views here.


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
# class FilmListAPIView(generics.ListAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer


# class FilmDetailAPIView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
