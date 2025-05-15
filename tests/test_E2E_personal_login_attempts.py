import pytest

def test_blocage_apres_5_tentatives(page, credentials_par, 
    for _ in range(6):
        page.goto(f"{base_url}/login")
        page.get_by_role("textbox", name="Nom de l'utilisateur").fill(credentials_par["email"])
        page.get_by_role("textbox", name="Mot de passe").fill("motdepassefaux")
        page.get_by_role("button", name="Connexion").click()
        # Vérifier clairement que l'alerte est bien visible
        assert page.get_by_role("alertdialog", name="mot de passe ou identifiant").is_visible(), \
        "L'alerte 'mot de passe ou identifiant' n'est pas affichée."


    
    page.goto(f"{base_url}/login")
    page.get_by_role("textbox", name="Nom de l'utilisateur").fill(credentials_par["email"])
    page.get_by_role("textbox", name="Mot de passe").fill(credentials_par["password"])
    page.get_by_role("button", name="Connexion").click()
    page.wait_for_load_state("networkidle")  # Attend que toutes les requêtes soient terminées
    page.screenshot(path="screenshot_attemps_pro_ko_approval.png")
    assert page.get_by_role("alertdialog", name="votre compte est bloqué").is_visible(), "Le compte n'est pas bloqué après 5 tentatives."
    
