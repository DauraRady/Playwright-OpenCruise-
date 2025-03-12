# tests/test_admin_login.py
import pytest
from pages.admin_management_page import AdminLoginPage

def test_admin_login(page, base_url, admin_credentials):
    # Instancier la page de login admin
    admin_page = AdminLoginPage(page)

    # 1. Aller sur la page de login admin
    admin_page.goto(base_url)

    # 2. Saisir les identifiants admin
    admin_page.login(
        username=admin_credentials["username"],
        password=admin_credentials["password"]
    )

    # 3. Vérifier la connexion
    assert admin_page.is_logged_in(), "La connexion admin a échoué"

    # 4. Capture d’écran
    page.screenshot(path="screenshot_admin_login.png")
