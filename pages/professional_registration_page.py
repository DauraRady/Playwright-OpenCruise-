# pages/professional_registration_page.py
class ProfessionalRegistrationPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_registration(self):
        # Après avoir cliqué sur "Vous n'avez pas de compte ?",
        self.page.get_by_role("link", name="Vous n'avez pas de compte ?").click()
        self.page.get_by_text("Professionnel").click()

    def fill_form(self, data: dict):
        self.page.get_by_role("textbox", name="Nom", exact=True).fill(data["last_name"])
        self.page.get_by_role("textbox", name="Prénom", exact=True).fill(data["first_name"])
        self.page.locator('//input[@formcontrolname="dateNaissance"]').nth(0).fill(data["birth_date"])
        self.page.get_by_role("textbox", name="Adresse", exact=True).fill(data["street_address"])
        self.page.get_by_role("combobox").first.select_option(label=data["country"])
        self.page.get_by_role("combobox").nth(1).select_option(label=data["city"])
        self.page.get_by_role("textbox", name="Code postal", exact=True).fill(data["postal_code"])
        self.page.get_by_role("textbox", name="Numéro de passeport").fill(data["passport_number"])
        self.page.get_by_role("textbox", name="Numéro de carte d’identité").fill(data["id_number"])
        self.page.get_by_role("textbox", name="Email").fill(data["email"])
        self.page.get_by_role("textbox", name="+").fill(data["phone"])
        self.page.get_by_role("textbox", name="Nouveau mot de passe *").fill(data["password"])
        self.page.get_by_role("textbox", name="Nouveau mot de passe", exact=True).fill(data["password"])
        self.page.get_by_role("combobox").nth(2).select_option("SNC")
        self.page.get_by_role("textbox", name="siret").fill(data["siret"])
        self.page.get_by_role("combobox").nth(3).select_option("50")

    def submit_form(self):
        self.page.get_by_role("button", name="Créer votre compte").click()

    def fill_representative_modal(self, data: dict):
        self.page.get_by_role("checkbox").check()
        modal = self.page.locator("#modalAddRepresentant")
        modal.get_by_role("textbox", name="Nom", exact=True).fill(data["nom"])
        modal.get_by_role("textbox", name="Prénom").fill(data["prenom"])
        modal.locator("input[type='date']").fill(data["birth_date"])
        modal.get_by_role("textbox", name="Adresse").fill(data["street_address"])
        modal.get_by_role("textbox", name="Code postal").fill(data["postal_code"])
        modal.locator("select[formcontrolname='currentPays']").select_option(label=data["country"])
        modal.locator("select[formcontrolname='ville']").select_option(label=data["city"])
        modal.get_by_role("textbox", name="Numéro de passeport").fill(data["passport_number"])
        modal.get_by_role("textbox", name="Numéro de carte d’identité").fill(data["id_number"])
        modal.get_by_role("textbox", name="Email").fill(data["email"])
        modal.get_by_role("textbox", name="+").fill(data["phone"])
        modal.locator("#user_password").fill(data["password"])
        modal.locator("#user_password_confirm").fill(data["password"])
        modal.get_by_role("combobox").nth(2).select_option("SA")
        modal.get_by_role("textbox", name="siret").fill(data["siret"])
        modal.get_by_role("combobox").nth(3).select_option("20")

    def submit_representative(self):
        self.page.locator("#modalAddRepresentant").get_by_role("button", name="Créer votre compte").click()

    
