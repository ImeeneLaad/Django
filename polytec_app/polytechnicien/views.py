from django.shortcuts import render, redirect
from django.contrib import messages  # Importe le module pour les messages
from .forms import MemberForm

def homepage(request):
    if request.method == "POST":
        print("✅ Formulaire soumis !")  
        print("📩 Données reçues :", request.POST)  

        # Crée une instance du formulaire avec les données POST et les fichiers
        form = MemberForm(request.POST, request.FILES)  

        if form.is_valid():
            print("🎉 Formulaire valide, enregistrement en cours...")
            form.save()  # Sauvegarde les données dans la base de données
            print("✅ Données enregistrées avec succès !")

            # Affiche un message de succès
            messages.success(request, 'Merci pour ton inscription !')

            # Redirige vers la même page pour vider le formulaire
            return redirect("homepage")  
        else:
            print("❌ Erreurs de validation :", form.errors)  # Debugging

            # Affiche les erreurs de validation sous forme de messages
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        # Affiche un formulaire vide pour les requêtes GET
        form = MemberForm()  

    # Rend la page avec le formulaire et les messages
    return render(request, "polytechnicien/index.html", {"form": form})  

def member_view(request, member_id):
    # Affiche la page d'un membre spécifique
    return render(request, "polytechnicien/member_view.html", {"member_id": member_id})