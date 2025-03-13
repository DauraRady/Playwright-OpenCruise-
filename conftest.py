# conftest.py
import os
import json
from faker import Faker
import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

# Charge le contenu du fichier .env
load_dotenv()
fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="ok", help="Environnement: ok ou ko")

@pytest.fixture(scope="session")
def base_url(pytestconfig):
    """
    Renvoie l'URL de base selon l'option --env.
    Si vous voulez pointer vers un environnement KO,
    modifiez le fichier .env ou créez-en un autre et changez la variable BASE_URL.
    """
    env = pytestconfig.getoption("env")
    if env.lower() == "ok":
        return os.getenv("BASE_URL_OK", "https://opencruise-ok.sogeti-center.cloud")
    elif env.lower() == "ko":
        return os.getenv("BASE_URL_KO", "https://opencruise-ko.sogeti-center.cloud")
    else:
        pytest.fail("Environnement inconnu. Utilisez 'ok' ou 'ko'.")

@pytest.fixture(scope="session")
def admin_credentials():
    """
    Récupère les identifiants admin depuis le .env.
    S'ils ne sont pas définis, on échoue directement.
    """
    username = os.getenv("ADMIN_USERNAME")
    password = os.getenv("ADMIN_PASSWORD")
    if not username or not password:
        pytest.fail("Les identifiants admin (ADMIN_USERNAME, ADMIN_PASSWORD) ne sont pas définis dans .env.")
    return {
        "username": username,
        "password": password
    }

@pytest.fixture(scope="session")
def credentials_par():
    fichier = "data/credentials_par.json"

    # Charger les données existantes si le fichier existe
    if os.path.exists(fichier):
        with open(fichier, encoding="utf-8") as f:
            credentials = json.load(f)
    else:
        credentials = {}  # Créer un dictionnaire vide si le fichier n'existe pas

    yield credentials  # Cette ligne permet à pytest d'utiliser la fixture

    # Sauvegarder les données mises à jour dans le fichier JSON
    with open(fichier, "w", encoding="utf-8") as f:
        json.dump(credentials, f, indent=4)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright

@pytest.fixture(scope="session")
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False,args=["--start-maximized"],slow_mo=800)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    # Toutes les vidéos seront enregistrées dans le dossier "videos"
    context = browser.new_context(record_video_dir="videos")
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    """
    Crée et fournit une nouvelle page pour chaque test.
    """
    page = context.new_page()
    yield page
