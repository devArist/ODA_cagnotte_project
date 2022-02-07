from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from . import models


@api_view(["GET"])
def home(request):

    return Response({"message": "Orange Digital Center"})


@api_view(["GET", "POST"])
def api_academicians(request):
    
    if request.method == 'GET':
        academician = models.Academician.objects.all()
        serializer = AcademicianSerializer(academician, many=True)
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        return Response({"message": "enregistrement"})
    
    
    
    
    
    