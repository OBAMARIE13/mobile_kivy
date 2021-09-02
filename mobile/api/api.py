from . import serializer
from mobile import models as models_mobile
from rest_framework import viewsets


class UtilisateurViewset(viewsets.ModelViewSet):
    queryset = models_mobile.Utilisateur.objects.filter(status=True)
    serializer_class = serializer.UtilisateurSerializer


class NoteViewset(viewsets.ModelViewSet):
    queryset = models_mobile.Note.objects.filter(status=True)
    serializer_class = serializer.NoteSerializer


class ContactViewset(viewsets.ModelViewSet):
    queryset = models_mobile.Contact.objects.filter(status=True)
    serializer_class = serializer.ContactSerializer
