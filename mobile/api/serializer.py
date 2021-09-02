from rest_framework import serializers 
from mobile import models as models_mobile 


class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_mobile.Utilisateur
        fields = '__all__'



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_mobile.Note
        fields = '__all__'



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models_mobile.Contact
        fields = '__all__'

