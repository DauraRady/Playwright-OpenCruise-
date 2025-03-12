# pages/admin_login_page.py
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
        Remplit les champs username/password et clique sur 'Login'.
        """
        self.page.get_by_role("textbox", name="Nom de l'utilisateur").fill(username)
        self.page.get_by_role("textbox", name="Mot de passe").fill(password)
        self.page.get_by_role("button", name="Connexion").click()
        self.page.wait_for_selector("text=Bienvenue formation admin", timeout=5000)
           
def logout(self):
    self.page.click("button:has-text('Se déconnecter')")
    # On attend qu'on revienne sur la page de connexion
    self.page.wait_for_selector("text=Connexion")

def navigate_to_user_list(self):
        # Exemple : via Settings > Utilisateurs > Lister les comptes
    self.page.click("text=settings")
    self.page.click("a:has-text('Utilisateurs')")
    self.page.click("a:has-text('Lister les comptes')")
    self.page.wait_for_selector("table")  # On attend qu'une table apparaisse

def approve_user(self, user_email: str):
        # Localiser la ligne de la table correspondant à l'email donné
    row = self.page.locator("tr", has_text=user_email)
        # Cliquer sur le bouton d'approbation dans cette ligne (ajustez le sélecteur selon votre application)
    row.locator("button:has-text('Approuver')").click()
        # On peut attendre un message de confirmation
    self.page.wait_for_selector("text=Compte approuvé")