import json
from faker import Faker
import pytest
import re
from pages.personal_registration_page import PersonalRegistrationPage
from pages.admin_management_page import AdminManagementPage

fake = Faker()

def load_data(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_e2e_personal_approval(page, base_url,credentials_par, admin_credentials):
    ''' TC01 création d'un compte particulier et approbation par l'admin '''
    # Charger les données depuis part.json
    personal_data = load_data("data/part.json")
    # Générer un email aléatoire
    generated_email = fake.email()
    personal_data["email"] = generated_email

    
    page.goto(f"{base_url}/login?returnUrl=%2F")
    personal_page = PersonalRegistrationPage(page)
    personal_page.navigate_to_registration()
    personal_page.fill_form(personal_data)
    personal_page.submit_form()
  
    credentials_par["email"] = generated_email
    credentials_par["password"] = personal_data["password"]  # mot de passe du JSON

    page.screenshot(path="screenshot_after_par_account_fill.png")

  
    page.wait_for_url(re.compile(".*login.*"), timeout=5000)
    assert "login" in page.url, "La redirection vers la page de login n'a pas eu lieu après la création du compte professionnel."
    page.screenshot(path="screenshot_after_par_account_creation.png")


    admin_page = AdminManagementPage(page)
    admin_page.goto(base_url)
    admin_page.login(admin_credentials["username"], admin_credentials["password"])
    admin_page.navigate_to_user_list()
    admin_page.approve_user(personal_data["first_name"], personal_data["last_name"], personal_data["email"])
    admin_page.logout()

    page.screenshot(path="screenshot_e2e_personal_approval.png")
 
    page.get_by_role("textbox", name="Nom de l'utilisateur").fill(personal_data["email"])
    page.get_by_role("textbox", name="Mot de passe").fill(personal_data["password"])
    page.get_by_role("button", name="Connexion").click()


    page.wait_for_selector("text=Bienvenue", timeout=5000)
    assert "Bienvenue" in page.content(), "La connexion avec le compte particulier créé a échoué."

    page.screenshot(path="screenshot_e2e_professional_approval.png")
