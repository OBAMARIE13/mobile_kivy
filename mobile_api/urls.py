"""mobile_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from mobile.api import api as mobile_api
from rest_framework import permissions


router = routers.DefaultRouter()

router.register('mobile/contact', mobile_api.ContactViewset, basename='api-contact')
router.register('mobile/utilisateur', mobile_api.UtilisateurViewset, basename='api-utilisateur')
router.register('mobile/note', mobile_api.NoteViewset, basename='api-note')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
