from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Member, CertificationRequest, Course, Event
from .forms import MemberForm, MemberRegistrationForm, CertificationRequestForm
from django.contrib.auth.hashers import make_password

def homepage(request):
    if request.method == "POST":
        print("✅ Formulaire soumis !")  
        print("📩 Données reçues :", request.POST)  

        registration_form = MemberRegistrationForm(request.POST, request.FILES)

        # Check if it's a registration form submission
        if registration_form.is_valid():
            member = registration_form.save(commit=False)
            member.set_password(registration_form.cleaned_data['password'])  # Hash the password
            member.save()
            messages.success(request, 'Inscription réussie! Veuillez attendre la validation de votre compte.')
            return redirect("homepage")  # Redirect after successful registration

        # Handle the regular form submission if registration form is invalid
        form = MemberForm(request.POST, request.FILES)

        if form.is_valid():
            print("🎉 Formulaire valide, enregistrement en cours...")
            form.save()
            print("✅ Données enregistrées avec succès !")
            messages.success(request, 'Merci pour ton inscription !')
            return redirect("homepage")  # Redirect after successful submission
        else:
            print("❌ Erreurs de validation :", form.errors)
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = MemberForm()

    return render(request, "polytechnicien/index.html", {"form": form})
def member_view(request, member_id):
    return render(request, "polytechnicien/member_view.html", {"member_id": member_id})

def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save(commit=False)
            member.set_password(form.cleaned_data['password'])  # Hachage du mot de passe
            member.save()
            messages.success(request, 'Inscription réussie! Veuillez attendre la validation de votre compte.')
            return redirect('certification_request')
    else:
        form = MemberRegistrationForm()
    


    return render(request, '/register.html', {'form': form})
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            member = Member.objects.get(email=email)
            if member.check_password(password):  # This will check the password correctly
                login(request, member)
                return redirect('home')  # Redirect to the home page after successful login
            else:
                messages.error(request, 'Identifiants invalides. Veuillez réessayer.')
        except Member.DoesNotExist:
            messages.error(request, 'Identifiants invalides. Veuillez réessayer.')

    return render(request, 'login/login.html')

@login_required
def certification(request):
    if request.method == 'POST':
        form = CertificationRequestForm(request.POST, request.FILES)
        if form.is_valid():
            cert_request = form.save(commit=False)
            cert_request.member = Member.objects.get(id=request.user.id)  # Assurez-vous que request.user est un Member
            cert_request.save()
            messages.success(request, 'Demande de certification envoyée avec succès!')
            return redirect('home')
    else:
        form = CertificationRequestForm()

    return render(request, 'certification/request.html', {'form': form})

@login_required
def home(request):
    courses = Course.objects.all().order_by('-created_at')
    events = Event.objects.all().order_by('-created_at')

    return render(request, 'home.html', {
        'courses': courses,
        'events': events
    })
