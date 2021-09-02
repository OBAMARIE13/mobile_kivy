from django.db import models

# Create your models here.

class Contact(models.Model):
    utilisateur = models.ForeignKey('mobile.Utilisateur', related_name='utilisateur_contact', on_delete=models.CASCADE)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    numero = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom


class Utilisateur(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    note = models.ForeignKey('mobile.Note', related_name='note_utilisateur', on_delete=models.CASCADE)
    contact = models.ForeignKey('mobile.Contact', related_name='contact_utilisateur', on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)


    class Meta():
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return self.nom


class Note(models.Model):
    titre = models.CharField(max_length=255, blank=True)
    texte = models.TextField()
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now_add=True)
