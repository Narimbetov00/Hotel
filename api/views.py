from django.shortcuts import render
from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .serializers import *
# Create your views here.


class HotelListAPIView(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = hotelserializer

class HotelCreateView(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = hotelserializer

class HotelRUD(RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = hotelserializer
    