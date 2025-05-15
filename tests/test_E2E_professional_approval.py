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
   
    prof_data_all = load_data("data/pro.json")
    
    professional_data = prof_data_all["professional"]
    representative_data = prof_data_all["representative"]

   
    generated_email = fake.email()
    professional_data["email"] = generated_email
    representative_data["email"] = generated_email

 
    page.goto(f"{base_url}/login?returnUrl=%2F")
    prof_page = ProfessionalRegistrationPage(page)
    prof_page.navigate_to_registration()
    prof_page.fill_form(professional_data)
    page.screenshot(path="screenshot_after_pro_account_fill.png")

   
    prof_page.fill_representative_modal(representative_data)
    prof_page.submit_representative()


    prof_page.submit_form()
    page.screenshot(path="erreur_creation_compte.png")
    allure.attach.file("erreur_creation_compte.png", name="Erreur technique site", attachment_type=allure.attachment_type.PNG)

    page.wait_for_url(re.compile(".*login.*"), timeout=15000)
    assert "login" in page.url, "La redirection vers la page de login n'a pas eu lieu après la création du compte pro."
    page.screenshot(path="screenshot_after_pro_account_creation.png")

    admin_page = AdminManagementPage(page)
    admin_page.goto(base_url)
    admin_page.login(admin_credentials["username"], admin_credentials["password"])
    admin_page.navigate_to_user_list()
    # Approuver le compte pro via professional_data (prénom, nom, email) - adaptez si besoin
    admin_page.approve_user(professional_data["first_name"], professional_data["last_name"], professional_data["email"])
    
   
    admin_page.logout()

  
    page.get_by_role("textbox", name="Nom de l'utilisateur").fill(professional_data["email"])
    page.get_by_role("textbox", name="Mot de passe").fill(professional_data["password"])
    page.get_by_role("button", name="Connexion").click()

    page.wait_for_selector("text=Bienvenue", timeout=5000)
    assert "Bienvenue" in page.content(), "La connexion avec le compte pro créé a échoué."

    page.screenshot(path="screenshot_e2e_professional_approval.png")
