import json
from faker import Faker
import pytest
from pages.personal_registration_page import PersonalRegistrationPage
from pages.admin_management_page import AdminManagementPage

fake = Faker()

def load_data(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_e2e_personal_approval(page, base_url, admin_credentials):
    # Charger les données depuis part.json
    personal_data = load_data("data/part.json")
    # Générer un email aléatoire
    generated_email = fake.email()
    personal_data["email"] = generated_email

    # Création du compte particulier
    page.goto(f"{base_url}/login?returnUrl=%2F")
    personal_page = PersonalRegistrationPage(page)
    personal_page.navigate_to_registration()
    personal_page.fill_form(personal_data)
    personal_page.submit_form()

    # Connexion en tant qu'admin et approbation du compte créé
    admin_page = AdminManagementPage(page)
    admin_page.goto(base_url)
    admin_page.login(admin_credentials["username"], admin_credentials["password"])
    admin_page.navigate_to_user_list()
    admin_page.approve_user(personal_data["first_name"], personal_data["last_name"], personal_data["email"])
    admin_page.logout()

    page.screenshot(path="screenshot_e2e_personal_approval.png")
