# 🎭 Guide Playwright avec Python (E2E & API Testing)

Ce guide fournit une configuration complète pour **Playwright avec Python**, en utilisant un environnement virtuel sous Windows. Il couvre l'installation, l'organisation en **Page Object Model (POM)**, la gestion des tests **Web et API**, les meilleures pratiques, ainsi qu'une comparaison avec **Selenium et Robot Framework**.

---

## 📋 1. Prérequis

- **Python 3.7+** ([Télécharger ici](https://www.python.org/downloads/))
- **pip** installé (inclus avec Python)
- **Git** installé ([Télécharger ici](https://git-scm.com/downloads))
- **Visual Studio Code** (optionnel mais recommandé)

---

## 🚀 2. Installation et Configuration

### 📌 2.1. Création d'un Environnement Virtuel (Windows)

```cmd
:: Création de l'environnement virtuel
python -m venv venv

:: Activation de l'environnement virtuel
venv\Scripts\activate
```

Pour désactiver l'environnement virtuel :

```cmd
deactivate
```

### 📌 2.2. Installation de Playwright et des Dépendances

```cmd
pip install playwright pytest pytest-playwright
```

Ensuite, installez les navigateurs pour Playwright :

```cmd
playwright install
```

Générez un fichier **requirements.txt** pour sauvegarder les dépendances :

```cmd
pip freeze > requirements.txt
```

Pour réinstaller les dépendances sur une autre machine :

```cmd
pip install -r requirements.txt
```

---

## 📂 3. Organisation du Projet (Frontend & Backend)

```
project/
│── tests/
│   ├── test_web.py
│   ├── test_api.py
│
│── pages/
│   ├── base_page.py
│   ├── sample_page.py
│
│── api/
│   ├── api_client.py
│
│── fixtures/
│   ├── test_data.json
│
│── conftest.py
│── pytest.ini
│── requirements.txt
│── .gitignore
│── README.md
```

### 📌 3.1. `.gitignore`

Ajoutez ce fichier pour éviter de suivre les fichiers inutiles avec Git :

```
venv/
__pycache__/
*.pyc  # Fichiers compilés Python
*.pyo  # Fichiers optimisés Python
*.log  # Fichiers de logs
```

---

## 🔎 4. Qu'est-ce que `sync_playwright` ?

📌 `sync_playwright` est la version **synchronisée** de Playwright pour exécuter des tests de manière simple et fluide en Python.

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://example.com")
    print(page.title())
    browser.close()
```

**Pourquoi utiliser `sync_playwright` ?**

- ✅ **Facile à lire et écrire** (comparé à `async_playwright` qui est asynchrone)
- ✅ **Pas besoin de gérer `async/await`** en Python
- ✅ **Idéal pour des scripts de test courts et efficaces**

---

## 🤖 5. Comparaison Playwright, Selenium et Robot Framework

| Outil               | Type      | Supporte les APIs | Langages supportés | Vitesse           |
| ------------------- | --------- | ----------------- | ------------------ | ----------------- |
| **Playwright**      | Web + API | ✅ Oui            | Python, JS, C#     | ⚡ Très rapide    |
| **Selenium**        | Web       | ❌ Non            | Python, Java, JS   | 🐢 Plus lent      |
| **Robot Framework** | Web + API | ✅ Oui (via libs) | Python             | 📜 Tests lisibles |

📌 **Pourquoi choisir Playwright ?**

- ✅ **Plus rapide que Selenium**
- ✅ **Support natif des tests API**
- ✅ **Meilleure gestion des sessions, cookies et authentification**

---

## 🌍 6. Tester les APIs avec Playwright

📌 **Playwright inclut sa propre API intégrée pour interagir avec des endpoints HTTP**. Contrairement à Postman, qui est un outil interactif, **Playwright permet d'automatiser ces tests directement dans un script Python**.

```python
from playwright.sync_api import sync_playwright

class APIClient:
    def __init__(self, request):
        self.request = request

    def get_user(self, user_id):
        response = self.request.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
        return response.json()

def test_get_user():
    with sync_playwright() as p:
        request = p.request.new_context()
        api_client = APIClient(request)
        user = api_client.get_user(1)
        assert user["id"] == 1
```

**Pourquoi utiliser Playwright plutôt que `requests` ?**

- ✅ **Gère les sessions utilisateur et cookies automatiquement**
- ✅ **Permet de tester Web + API sans outils supplémentaires**
- ✅ **Exécute les requêtes en mode **headless** (sans navigateur visible)**

---

## 📜 7. Exécution des Tests avec `pytest`

📌 **Tous les tests sont exécutés avec `pytest`**.

### **Exécuter les tests `pytest` :**

```cmd
pytest tests/
```

📌 **Organisation des tests**

- **Utiliser `pytest`** pour des tests unitaires et fonctionnels.
- **Ne pas utiliser `behave`** (pas nécessaire si BDD non requise).

---

## 🎯 8. Commandes Essentielles Playwright

- **Lancer un test spécifique** :

```cmd
pytest tests/test_web.py
```

- **Voir le rapport HTML** :

```cmd
pytest --html=report.html
```

- **Ouvrir un navigateur interactif** :

```cmd
playwright open example.com
```

- **Mode debug (enregistreur automatique)** :

```cmd
playwright codegen example.com
```

---

## ✅ 9. Conclusion

Ce guide permet de :

- **Comprendre `sync_playwright` et son fonctionnement**
- **Installer et configurer Playwright pour les tests Web et API**
- **Utiliser uniquement `pytest` pour exécuter les tests**
- **Tester les APIs avec Playwright au lieu de Postman**
- **Utiliser Playwright de manière efficace en automatisation**

🚀 **Playwright est l'outil idéal pour des tests E2E modernes et rapides !**

# README - Playwright et les Attentes Automatiques

## 🎯 Playwright attend-il automatiquement ?

✅ **Oui, Playwright attend automatiquement jusqu'à 30 secondes** pour certaines actions comme `click()`, `fill()`, `goto()`, etc.
👉 Ce délai s'appelle le **timeout** et vaut `30 000 ms` par défaut.

💡 **Si l’élément apparaît avant 30 secondes, Playwright continue immédiatement.**
💡 **Si l’élément n’apparaît pas dans ce délai, Playwright plante avec une erreur.**

🔧 **Modifier ce délai par défaut :**

```python
await page.click("#bouton", timeout=10000)  # Attend max 10 sec avant de planter
```

---

## 📌 Quand faut-il utiliser `wait_for_selector()` ?

Playwright attend déjà automatiquement, **mais pas toujours dans les cas suivants** :

### 🔹 **1. L’élément met du temps à apparaître (AJAX, chargement dynamique)**

👉 **Problème :** Si l’élément est chargé après un délai, Playwright peut essayer d'interagir avec lui trop tôt.

```python
await page.click("#search-button")
await page.click("#result-item")  # ⚠️ Peut échouer si les résultats ne sont pas encore affichés !
```

✅ **Solution :** Attendre l’apparition de l’élément avant d’interagir avec lui.

```python
await page.wait_for_selector("#result-item")  # 🔥 Attend que l'élément soit là
await page.click("#result-item")  # ✅ Plus de problème !
```

---

### 🔹 **2. L’élément est caché (`display: none`) et devient visible plus tard**

👉 **Problème :** Un élément est bien présent dans le DOM, mais invisible (`display: none`).

```python
await page.click("#mon-bouton")  # ⚠️ Échec si le bouton est caché !
```

✅ **Solution :** Attendre qu’il devienne **visible** avant de cliquer.

```python
await page.wait_for_selector("#mon-bouton", state="visible")  # 🔥 Attend qu’il s’affiche
await page.click("#mon-bouton")  # ✅ Plus d'erreur !
```

---

### 🔹 **3. Un loader (spinner) bloque les interactions**

👉 **Problème :** Un **loader** s'affiche pendant le chargement et empêche d’interagir avec la page.

```python
await page.click("#mon-bouton")  # ⚠️ Échec si le loader masque le bouton !
```

✅ **Solution :** Attendre que le loader disparaisse avant d’agir.

```python
await page.wait_for_selector("#loader", state="hidden")  # 🔥 Attend que le loader disparaisse
await page.click("#mon-bouton")  # ✅ Fonctionne maintenant !
```

---

## 🔎 **Comment savoir si un élément est un cas particulier ?**

1️⃣ **Ouvre DevTools (`F12` sur Chrome).**
2️⃣ **Inspecte l’élément et regarde s’il est déjà dans le DOM.**
3️⃣ **Si l’élément n’existe pas immédiatement → `wait_for_selector()`.**
4️⃣ **Si l’élément est dans le DOM mais `display: none` → `state="visible"`.**
5️⃣ **Si un loader masque un bouton → `state="hidden"`.**

---

## 📌 **Résumé des cas où `wait_for_selector()` est nécessaire**

| **Situation**                               | **Besoin de `wait_for_selector()` ?** | **Explication**                    |
| ------------------------------------------- | ------------------------------------- | ---------------------------------- |
| Un élément est chargé après un délai (AJAX) | ✅ OUI                                | Il n’est pas dans le DOM au départ |
| Un pop-up apparaît après un clic            | ✅ OUI                                | Il n’existe pas au début           |
| Un loader masque un bouton                  | ✅ OUI                                | Attendre que le loader disparaisse |
| Un élément est déjà visible dès le départ   | ❌ NON                                | Playwright attend tout seul        |

---

## 🎯 **Règle d’or pour savoir si `wait_for_selector()` est nécessaire**

👉 **Si ton test échoue avec "element not found" ou "not visible", utilise `wait_for_selector()`.**
👉 **Si tu vois l’élément dans DevTools mais que Playwright ne le trouve pas, il est sûrement caché → utilise `state="visible"`.**

---

😃 **Avec ces règles, tes tests Playwright seront plus fiables et stables ! 🚀**
