import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

from .models import Covid19
from .serializers import Covid19Serializer

class Covid19ListView(ListCreateAPIView):
    queryset=Covid19.objects.all()
    serializer_class= Covid19Serializer

class Covid19DetailView(RetrieveUpdateDestroyAPIView):
    queryset=Covid19.objects.all()
    serializer_class=Covid19Serializer 

class WorldTotalStatistics(APIView):
    def get(self,format=None):
        res = requests.get('https://api.covid19api.com/world/total').json()
        return Response(res)
        

class LocalStatistics(APIView):
        def get(self,request,format=None):
            Country=request.GET['country']
            From=request.GET["from"]
            to=request.GET['to']
            url=f'https://api.covid19api.com/country/{Country}/status/confirmed?from={From}&to={to}'
            res = requests.get(url).json()
            return Response(res)

class Summary(APIView):
        serializer_class=Covid19Serializer
        def get(self,format=None):
            url='https://api.covid19api.com/summary'
            r = requests.get(url).json()
            return Response(r)
        
