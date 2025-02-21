from django import forms
from .models import Member, CertificationRequest  # Adjust according to your models

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = (
            "full_name", "email", "twitter", "linkedin", "facebook",
            "website", "picture", "bio", "city", "github", "instagram", "title",
        )

class MemberRegistrationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['email', 'password', 'full_name']  # Add relevant fields here

class CertificationRequestForm(forms.ModelForm):
    class Meta:
        model = CertificationRequest  # Ensure this matches your model
        fields = ['member', 'cv', 'diploma', 'motivation_letter']  # Define your fields here
