# pages/admin_management_page.py

class AdminManagementPage:
    def __init__(self, page):
        self.page = page

    def goto(self, base_url: str):
        """
        Va directement sur la page de login admin.
        """
        self.page.goto(base_url)

    def login(self, username: str, password: str):
        """
        Remplit les champs username/password et clique sur 'Connexion'.
        """
        self.page.get_by_role("textbox", name="Nom de l'utilisateur").fill(username)
        self.page.get_by_role("textbox", name="Mot de passe").fill(password)
        self.page.get_by_role("button", name="Connexion").click()
        self.page.wait_for_selector("text=Bienvenue formation admin", timeout=5000)

    def logout(self):
        """
        Se déconnecte et attend le retour sur la page de connexion.
        """
        self.page.get_by_role("button", name="Bienvenue formation admin").click()
        self.page.get_by_role("button", name="Se déconnecter").click()
        locator = self.page.get_by_role("img", name="OpenCruise oce")
        locator.wait_for()
        assert locator.is_visible(), "L'image 'OpenCruise oce' n'est pas visible après la déconnexion."

    def navigate_to_user_list(self):
        """
        Navigue via Settings > Utilisateurs > Lister les comptes.
        """
        self.page.click("text=settings")
        self.page.click("a:has-text('Utilisateurs')")
        self.page.click("a:has-text('Lister les comptes')")
        self.page.wait_for_selector("table")  # On attend qu'une table apparaisse

    def approve_user(self, user_email: str):
        """
        Localise la ligne de la table correspondant à l'email donné et clique sur le bouton 'Approuver'.
        """
        self.page.get_by_role("row", name="miu miu moustik@").locator("a").first.click()

    def approve_user(self, first_name: str, last_name: str, email: str):
        email_prefix = email.split("@")[0]
        row_name = f"{first_name} {last_name} {email_prefix}@"
        row = self.page.get_by_role("row", name=row_name)
        row.scroll_into_view_if_needed()
        row.locator("a").first.click()
        