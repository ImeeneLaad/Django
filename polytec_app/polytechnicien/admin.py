from django.contrib import admin
from .models import Member  # Import du modèle

# Enregistrement du modèle pour qu'il apparaisse dans Django Admin
admin.site.register(Member)
