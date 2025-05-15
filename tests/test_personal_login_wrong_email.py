import pytest

def test_inscription_email_invalide(page, base_url):
    
    page.goto(f"{base_url}/login")  


    page.get_by_role("textbox", name="Nom de l'utilisateur").fill("email-invalide.com")
    page.get_by_role("textbox", name="Mot de passe").fill("Motdepasse123!")
    page.get_by_role("button", name="Connexion").click()
    

    assert page.get_by_role("alertdialog", name="mot de passe ou identifiant").is_visible(), \
        "L'alerte 'mot de passe ou identifiant' n'est pas affichée."
