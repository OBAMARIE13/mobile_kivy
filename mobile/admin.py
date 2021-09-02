from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('utilisateur', 'nom', 'prenom', 'email', 'numero', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'

@admin.register(models.Note)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('titre', 'texte', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'


@admin.register(models.Utilisateur)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'contact', 'note', 'email', 'date_add', 'date_update', 'status')
	date_hierarchy = 'date_add'
