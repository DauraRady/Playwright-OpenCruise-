# tests/test_personal_registration.py
import json
from faker import Faker
import pytest
from pages.personal_registration_page import PersonalRegistrationPage

fake = Faker()

def load_data(path: str):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_personal_registration(page, base_url):
    personal_data = load_data("data/part.json")
    personal_data["email"] = fake.email()
    
    page.goto(f"{base_url}/login?returnUrl=%2F")
    
    personal_page = PersonalRegistrationPage(page)
    personal_page.navigate_to_registration()
    personal_page.fill_form(personal_data)
    page.screenshot(path="screenshot_personal_post_final.png")
    personal_page.submit_form()
    
    page.screenshot(path="screenshot_personal_final.png")
