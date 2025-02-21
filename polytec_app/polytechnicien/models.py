from django.db import models
from uuid import uuid4
from django.contrib.auth.hashers import make_password, check_password
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin  # Add this import for permissions

def upload_picture(instance, filename):
    extension = filename.split('.')[-1]  # Récupère l'extension du fichier (ex: 'jpg', 'png')
    return 'static/uploads/members/{}.{}'.format(uuid4().hex, extension)  # Renvoie un chemin unique
class MemberManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
class Member(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # Add password field with encryption
    password = models.CharField(max_length=128)  # Using 128 for hashed password storage
    title = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    twitter = models.CharField(max_length=255, null=True, blank=True)
    linkedin = models.CharField(max_length=255, null=True, blank=True)
    facebook = models.CharField(max_length=255, null=True, blank=True)
    instagram = models.CharField(max_length=255, null=True, blank=True)
    website = models.CharField(max_length=255, null=True, blank=True)
    picture = models.FileField(upload_to=upload_picture, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(null=True, blank=True)  # Add last_login field
    objects = MemberManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name']  # Adjust as necessary

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        # Hash password if it's being set for the first time
        if self._state.adding:  # Hash only if the password is being set for the first time
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    
class CertificationRequest(models.Model):
    STATUS_CHOICES = (
        ('pending', 'En attente'),
        ('validated', 'Validé'),
        ('rejected', 'Rejeté')
    )
    
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    validation_date = models.DateTimeField(null=True, blank=True)
    certificate_number = models.CharField(max_length=50, unique=True, null=True)
    
    # Documents required for certification
    cv = models.FileField(upload_to='certifications/cv/')
    diploma = models.FileField(upload_to='certifications/diplomas/')
    motivation_letter = models.FileField(upload_to='certifications/letters/')
    
    def generate_certificate_number(self):
        return f"CERT-{uuid4().hex[:8].upper()}"
    
    def validate_certification(self):
        self.status = 'validated'
        self.validation_date = timezone.now()
        self.certificate_number = self.generate_certificate_number()
        self.save()

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    image = models.ImageField(upload_to='courses/')
    instructor = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    organizer = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


