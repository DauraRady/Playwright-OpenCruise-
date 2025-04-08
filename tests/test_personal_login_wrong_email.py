import pytest

def test_inscription_email_invalide(page, base_url):
    """
    TC02 - Vérifier que le système affiche une erreur 
    lorsque l'utilisateur saisit un email invalide à l'inscription.
    """
    page.goto(f"{base_url}/login")  # Remplace "/register" par l'URL exacte d'inscription perso

    # Remplir le formulaire avec un email invalide
    page.get_by_role("textbox", name="Nom de l'utilisateur").fill("email-invalide.com")
    page.get_by_role("textbox", name="Mot de passe").fill("Motdepasse123!")
    page.get_by_role("button", name="Connexion").click()
    

    # Vérifier l'affichage du message d'erreur lié à l'email
    assert page.get_by_role("alertdialog", name="mot de passe ou identifiant").is_visible(), \
        "L'alerte 'mot de passe ou identifiant' n'est pas affichée."