from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    CREATOR = "CREATOR"
    SUSCRIBER = "SUSCRIBER"

    ROLES_CHOICES = (
    (CREATOR, "Createur"), 
    (SUSCRIBER, "Abonné"),              
   )                
    profil_photo = models.ImageField()
    role = models.CharField(max_length=30, choices=ROLES_CHOICES)

