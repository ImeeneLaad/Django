from django.db import models
from uuid import uuid4


def upload_picture(instance, filename):
    extension = filename.split('.')[-1]  # Récupère l'extension du fichier (ex: 'jpg', 'png')
    return 'static/uploads/members/{}.{}'.format(uuid4().hex, extension)  # Renvoie un chemin unique



class Member(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=255, null=True, blank=True)  # Ajouté
    bio = models.TextField(null=True, blank=True)  # Ajouté
    city = models.CharField(max_length=255, null=True, blank=True)  # Ajouté
    github = models.CharField(max_length=255, null=True, blank=True)  # Ajouté
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)  # Ajouté
    website = models.CharField(max_length=255, null=True, blank=True)
    picture = models.FileField(upload_to=upload_picture, null=True)  # Utilise la fonction upload_picture

    def __str__(self):
        return self.full_name
