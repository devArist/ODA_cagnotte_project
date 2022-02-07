from rest_framework import serializers
from . import models

class AcademicianSerializer(serializers.ModelSerializer):
    
    class EmbendedSerializer(serializers.ModelSerializer):
        class Meta:
            model = models.Caisse
            fields = ('id','montant', 'status')
            
    caisse_academicien = EmbendedSerializer(many=True)
    
    class Meta:
        model = models.Academician
        exclude = ["date_update", "date_add"]
        
        
        
class CaisseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Caisse
        exclude = ["date_update", "date_add"]
        depth = 1 