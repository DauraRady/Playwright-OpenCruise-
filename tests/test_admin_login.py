# tests/test_admin_login.py
import pytest
from pages.admin_management_page import AdminManagementPage

def test_admin_login(page, base_url, admin_credentials):
    # Instancier la classe AdminManagementPage avec la page Playwright
    admin_page = AdminManagementPage(page)

    # Aller sur la page de login admin
    admin_page.goto(base_url)

    # Se connecter avec les identifiants admin
    admin_page.login(admin_credentials["username"], admin_credentials["password"])

    # Capture d'écran pour la preuve
    page.screenshot(path="screenshot_admin_login.png")
