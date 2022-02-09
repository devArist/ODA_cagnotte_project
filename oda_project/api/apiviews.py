from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from . import models
from rest_framework import status
from managers import api_pagination
from datetime import date


def academician_exists(registration_number):
    try:
        academician = models.Academician.objects.get(registration_number=registration_number)
        return True
    except models.Academician.DoesNotExist:
        return False


@api_view(["GET"])
def home(request):

    return Response({"message": " Bienvenue à Orange Digital Center"})


@api_view(["GET", "POST"])
def api_academicians(request):
    message = ""
    success = False

    if request.method == "GET":
        academician = models.Academician.objects.all()
        # serializer = AcademicianSerializer(academician, many=True)

        # return Response(serializer.data)
        return api_pagination.academician_pagination(academician, request)

    elif request.method == "POST":
        if academician_exists(request.data.get('registration_number')):
            message = 'Cet académicien est déjà inscrit !'
            return Response({'message': message, 'success': success})
        else:
            serializer = AcademicianSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                message = 'Académicien bien enregistré.'
                success = True
                return Response({'message': message, 'success': success}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    message = "Erreur: mauvaise requête"
    return Response({"message":message, "success": success}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def api_academician(request, registration_number: str):
    message = ""
    success = False
    # try:
    #         academician = models.Academician.objects.get(registration_number=registration_number)
    # except models.Academician.DoesNotExist:
    #     return Response(
    #         {"Erreur": "Académicien introuvable !"},
    #         status=status.HTTP_404_NOT_FOUND,
    #     )
    
    if not academician_exists(registration_number):
        message = 'Erreur: Académicien introuvable !'
        return Response({'message': message, 'success': success})
    else: academician = models.Academician.objects.get(registration_number=registration_number)
    
    if request.method == "GET":
        serializer = AcademicianSerializer(academician)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = AcademicianSerializer(academician, request.data)

        if serializer.is_valid():
            serializer.save()
            message = 'Modification éffectuée avec succès.'
            success = True
            return Response({'message': message, 'success': success}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        academician.delete()
        message = 'Académicien bien supprimé !'
        success = True

    return Response({"message":message, "success": success}, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "POST"])
def api_payment(request, registration_number: str):
    message = ""
    success = False
    
    if not academician_exists(registration_number):
        message = 'Erreur: Académicien introuvable !'
        return Response({'message': message, 'success': success})
    else: academician = models.Academician.objects.get(registration_number=registration_number)
    
    
    if request.method == 'GET':
        serializer = AcademicianSerializer(academician)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        today = date.today()
        for d in academician.caisse_academicien.all():
            if today.strftime('%Y-%m-%d') == d.payment_date:
                message = "Paiement déjà éffectué pour aujourd'hui !"
                
                return Response({'message': message, 'success': success})
        
        caisse = models.Caisse(
            academician=academician,
            reason=request.data.get('reason'),
            amount=request.data.get('amount'),
        )
        academician_serializer = AcademicianSerializer(academician)
        serializer = CaisseSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            message = 'Paiement bien effectué',
            success = True
            
            return Response({'message': message, 'success': success}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)