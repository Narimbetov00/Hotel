from rest_framework import serializers
from hotel.models import *

class hotelserializer(serializers.ModelSerializer):
    class Meta:

        model = Hotel
        fields = '__all__'
