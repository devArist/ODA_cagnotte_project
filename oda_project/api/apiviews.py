from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from . import models
from rest_framework import status


@api_view(["GET"])
def home(request):

    return Response({"message": " Bienvenue à Orange Digital Center"})


@api_view(["GET", "POST"])
def api_academicians(request):

    if request.method == "GET":
        academician = models.Academician.objects.all()
        serializer = AcademicianSerializer(academician, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        serializer = AcademicianSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    return Response({"Error": "Bad request !"})


@api_view(["GET", "PUT", "DELETE"])
def api_academician(request, pk: int):
    try:
            academician = models.Academician.objects.get(pk=pk)
    except models.Academician.DoesNotExist:
        return Response(
            {"Erreur": "Académicien introuvable !"},
            status=status.HTTP_404_NOT_FOUND,
        )
        
    
    if request.method == "GET":
        serializer = AcademicianSerializer(academician)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = AcademicianSerializer(academician, request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        try:
            academician.delete()
            return Response(
                {"message": "Académicien bien supprimé."}, status=status.HTTP_200_OK
            )
        except models.Academician.DoesNotExist:
            return Response(
                {"Erreur": "Académicien introuvable !"},
                status=status.HTTP_404_NOT_FOUND,
            )

    return Response({"Error": "Bad request !"}, status=status.HTTP_400_BAD_REQUEST)
