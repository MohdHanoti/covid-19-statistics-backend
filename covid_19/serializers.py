from rest_framework import serializers
from .models import Covid19

class Covid19Serializer(serializers.ModelSerializer):

    class Meta:
        model = Covid19 
        fields = ('Country', 'Confirmed', 'Deaths', 'Recovered', 'Date')