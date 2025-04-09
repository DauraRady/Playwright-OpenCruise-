import json
import re
from faker import Faker
import pytest
from pages.professional_registration_page import ProfessionalRegistrationPage
from pages.admin_management_page import AdminManagementPage

fake = Faker()

def load_data(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_e2e_professional_approval(page, base_url, admin_credentials):
    """
    TC07 - Vérifier la création d'un compte professionnel et son approbation par l'admin.
    1) Crée un compte Professionnel (avec représentant)
    2) Vérifie la redirection vers la page login
    3) Connexion en tant qu'admin + approbation du compte
    4) Déconnexion admin
    5) Connexion avec le compte pro créé
    """

    # Charger les données depuis pro.json
    prof_data_all = load_data("data/pro.json")
    # Suppose qu'on a 2 clés : "professional" et "representative"
    professional_data = prof_data_all["professional"]
    representative_data = prof_data_all["representative"]

    # Générer un email aléatoire pour le professionnel
    generated_email = fake.email()
    professional_data["email"] = generated_email

    # 1) Création du compte Professionnel
    page.goto(f"{base_url}/login?returnUrl=%2F")
    prof_page = ProfessionalRegistrationPage(page)
    prof_page.navigate_to_registration()
    prof_page.fill_form(professional_data)
    page.screenshot(path="screenshot_after_pro_account_fill.png")

    # Remplir le modal représentant
    prof_page.fill_representative_modal(representative_data)
    prof_page.submit_representative()

    # Finaliser
    prof_page.submit_form()

    # 2) Vérifier la redirection vers la page login
    page.wait_for_url(re.compile(".*login.*"), timeout=15000)
    assert "login" in page.url, "La redirection vers la page de login n'a pas eu lieu après la création du compte pro."
    page.screenshot(path="screenshot_after_pro_account_creation.png")

    # 3) Connexion en tant qu'admin et approbation
    admin_page = AdminManagementPage(page)
    admin_page.goto(base_url)
    admin_page.login(admin_credentials["username"], admin_credentials["password"])
    admin_page.navigate_to_user_list()
    # Approuver le compte pro via professional_data (prénom, nom, email) - adaptez si besoin
    admin_page.approve_user(professional_data["first_name"], professional_data["last_name"], professional_data["email"])
    
    # 4) Déconnexion admin
    admin_page.logout()

    # 5) Connexion avec le compte pro créé
    page.get_by_role("textbox", name="Nom de l'utilisateur").fill(professional_data["email"])
    page.get_by_role("textbox", name="Mot de passe").fill(professional_data["password"])
    page.get_by_role("button", name="Connexion").click()

    # Vérifier la connexion
    page.wait_for_selector("text=Bienvenue", timeout=5000)
    assert "Bienvenue" in page.content(), "La connexion avec le compte pro créé a échoué."

    page.screenshot(path="screenshot_e2e_professional_approval.png")
