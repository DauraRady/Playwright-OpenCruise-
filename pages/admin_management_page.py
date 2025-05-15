

class AdminManagementPage:
    def __init__(self, page):
        self.page = page

    def goto(self, base_url: str):
       
        self.page.goto(base_url)

    def login(self, username: str, password: str):
       
        self.page.get_by_role("textbox", name="Nom de l'utilisateur").fill(username)
        self.page.get_by_role("textbox", name="Mot de passe").fill(password)
        self.page.get_by_role("button", name="Connexion").click()
        self.page.wait_for_selector("text=Bienvenue formation admin", timeout=5000)

    def logout(self):
        
        self.page.get_by_role("button", name="Bienvenue formation admin").click()
        self.page.get_by_role("button", name="Se déconnecter").click()
        locator = self.page.get_by_role("img", name="OpenCruise oce")
        locator.wait_for()
        assert locator.is_visible(), "L'image 'OpenCruise oce' n'est pas visible après la déconnexion."

    def navigate_to_user_list(self):
        
        self.page.click("text=settings")
        self.page.click("a:has-text('Utilisateurs')")
        self.page.click("a:has-text('Lister les comptes')")
        self.page.wait_for_selector("table")  # On attend qu'une table apparaisse

    def approve_user(self, user_email: str):
        
        self.page.get_by_role("row", name="miu miu moustik@").locator("a").first.click()

    def approve_user(self, first_name: str, last_name: str, email: str):
        email_prefix = email.split("@")[0]
        row_name = f"{first_name} {last_name} {email_prefix}@"
        row = self.page.get_by_role("row", name=row_name)
        row.scroll_into_view_if_needed()
        row.locator("a").first.click()
        
