# tests/test_professional_registration.py
import json
from faker import Faker
import pytest
from pages.professional_registration_page import ProfessionalRegistrationPage

fake = Faker()

def load_data(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_professional_registration(page, base_url):
    # Charger les données depuis pro.json
    data = load_data("data/pro.json")
    prof_data = data["professional"]
    rep_data = data["representative"]
    
    # Générer des emails aléatoires
    prof_data["email"] = fake.email()
    rep_data["email"] = fake.email()
    
    page.goto(f"{base_url}/login?returnUrl=%2F")
    
    reg_page = ProfessionalRegistrationPage(page)
    reg_page.navigate_to_registration()
    reg_page.fill_form(prof_data)
  
    
    reg_page.fill_representative_modal(rep_data)
    page.screenshot(path="screenshot_rep_professional_final.png")
    reg_page.submit_representative()
    page.screenshot(path="screenshot_professional_post_final.png")
    reg_page.submit_form()
    
    page.screenshot(path="screenshot_professional_final.png")
