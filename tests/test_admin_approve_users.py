# tests/test_admin_approve_users.py
import pytest
from pages.admin_management_page import AdminManagementPage

def test_admin_approve_users(page, base_url, admin_credentials):
    admin_page = AdminManagementPage(page)
    # Connexion en tant qu'admin
    admin_page.login(base_url, admin_credentials["username"], admin_credentials["password"])
    # Naviguer vers la liste des comptes
    admin_page.navigate_to_user_list()
    # Approver un compte utilisateur (ici, par exemple, "user@example.com")
    admin_page.approve_user("moustik@snoopy.com")
    # Déconnexion
    admin_page.logout()
