# pages/personal_registration_page.py
import re
class PersonalRegistrationPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_registration(self):
        self.page.get_by_role("link", name="Vous n'avez pas de compte ?").click()
        self.page.get_by_text("Particulier").click()
        self.page.locator("div").filter(has_text=re.compile(r"^Particulier$")) \
        .get_by_role("radio").check()

    def fill_form(self, data: dict):
        # Champs principaux du titulaire
        self.page.get_by_role("textbox", name="Nom", exact=True).fill(data["last_name"])
        self.page.get_by_role("textbox", name="Prénom", exact=True).fill(data["first_name"])
        self.page.locator('//input[@formcontrolname="dateNaissance"]').nth(0).fill(data["birth_date"])
        self.page.get_by_role("textbox", name="Adresse", exact=True).fill(data["street_address"])
        self.page.get_by_role("textbox", name="Code postal", exact=True).fill(data["postal_code"])
        self.page.get_by_role("combobox").first.select_option(label=data["country"])
        self.page.get_by_role("combobox").nth(1).select_option(label=data["city"])
        self.page.get_by_role("textbox", name="Email", exact=True).fill(data["email"])
        self.page.get_by_role("textbox", name="+").fill(data["phone"])
        self.page.get_by_role("textbox", name="Nouveau mot de passe *").fill(data["password"])
        self.page.get_by_role("textbox", name="Nouveau mot de passe", exact=True).fill(data["password"])
        
        # Champs supplémentaires pour le titulaire
        if "passport_number" in data:
            self.page.get_by_role("textbox", name="Numéro de passeport").fill(data["passport_number"])
        if "id_number" in data:
            self.page.get_by_role("textbox", name="Numéro de carte d’identité").fill(data["id_number"])
        
        # Champs pour le conjoint (si présents dans le fichier de données)
        if "spouse_last_name" in data:
            self.page.get_by_role("textbox", name="Nom du conjoint", exact=True).fill(data["spouse_last_name"])
        if "spouse_first_name" in data:
            self.page.get_by_role("textbox", name="Prénom du conjoint").fill(data["spouse_first_name"])
        if "spouse_birth_date" in data:
            self.page.locator('//input[@formcontrolname="dateNaissanceConjoint"]').fill(data["spouse_birth_date"])

    def submit_form(self):
        self.page.get_by_role("button", name="Créer votre compte").click()
