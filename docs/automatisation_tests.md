# 📌 Projet d'Automatisation des Tests Playwright

## 📝 Introduction

Ce projet implémente une suite de tests automatisés en utilisant **Playwright** et **pytest** pour valider les fonctionnalités critiques de l'application OpenCruise. Les tests sont organisés selon une approche **Page Object Model (POM)** afin d'améliorer la maintenance et la réutilisabilité du code.

---

## 🖥️ Technologies et Frameworks Utilisés

- **Langage :** Python 🐍
- **Framework de test :** Pytest 🧪
- **Automatisation UI :** Playwright 🎭
- **Génération de rapports :** Allure Report 📊
- **Gestion des dépendances :** `pip` 📦
- **Gestion des environnements :** `.env` 🔐

---

## 📂 Structure du Projet

- **`pages/`** : Contient les classes représentant chaque page de l'application (POM).
- **`tests/`** : Contient les tests automatisés.
- **`data/`** : Contient les fichiers JSON utilisés pour stocker les informations des comptes.
  - `credentiels_par.json` : Stocke les identifiants des comptes créés en environnement OK.
  - `part.json` : Contient les données utilisées pour la création de comptes particuliers.
  - `pro.json` : Contient les données utilisées pour la création de comptes professionnels.
- **`.env`** : Fichier contenant les identifiants admin pour les tests d'approbation.
- **`conftest.py`** : Déclare les fixtures utilisées dans pytest.
- **`requirements.txt`** : Liste des dépendances requises.
- **`rapport de campagne.md`** : Suivi des tests effectués.
- **`allure-results/`** : Dossier contenant les résultats des tests pour la génération des rapports Allure.

---

## 🏗️ Explication du POM (Page Object Model)

Le projet suit le modèle POM où chaque page de l'application est représentée par une classe qui regroupe :

- **Les locators des éléments UI**.
- **Les méthodes pour interagir avec ces éléments** (ex: remplir un formulaire, cliquer sur un bouton).

Cela permet :
✅ Une meilleure séparation entre logique métier et implémentation des tests.
✅ Une meilleure maintenabilité (modifications locales en cas de changements UI).
✅ Une réutilisation facile dans plusieurs tests.

---

## ⚙️ Explication des Fixtures dans `conftest.py`

Les fixtures permettent de gérer les prérequis des tests de manière **automatisée** et **réutilisable**.

### 🔹 `credentiels_par`

- **Rôle** : Stocke et récupère les identifiants des comptes créés en environnement OK.
- **Lien avec pytest** : Cette fixture est injectée automatiquement dans les tests pour éviter d'avoir à recréer manuellement des comptes.
- **Lien avec Playwright** : Utilisée pour récupérer les identifiants stockés et les utiliser dans les tests de connexion.
- **Stockage dans un fichier JSON (`data/credentiels_par.json`)** :
  - Lorsqu'un compte est créé en **env OK**, l'email et le mot de passe sont **enregistrés** dans ce fichier.
  - Lors des tests en **env KO**, ces identifiants sont **chargés** pour réutilisation, car la création de compte n'est pas possible en KO.

### 🔹 `admin_credentials`

- **Rôle** : Contient les informations de connexion de l'administrateur pour la gestion des approbations.

### 🔹 Fixtures Playwright : `browser`, `context`, `page`

- **`browser`** : Lance un navigateur Playwright.
- **`context`** : Crée un contexte de navigation (gère les cookies et sessions utilisateur).
- **`page`** : Ouvre une page web pour exécuter les tests UI.

---

## 🚀 Exécution des Tests

### 1️⃣ **Créer un compte en environnement OK**

```bash
pytest --env OK tests/test_E2E_personal_approval.py
```

### 2️⃣ **Tester la connexion après blocage en environnement KO**

```bash
pytest --env KO tests/test_personal_login_attempts.py
```

### 3️⃣ **Tester la création et l'approbation d'un compte professionnel**

```bash
pytest --env OK tests/test_E2E_professional_approval.py
```

### 4️⃣ **Générer un rapport Allure après exécution des tests**

```bash
allure serve allure-results
```

Cette commande ouvre automatiquement le rapport des tests dans un navigateur.

---

## 📦 Dépendances Requises

Avant d'exécuter les tests, assurez-vous d'installer toutes les dépendances avec :

```bash
pip install -r requirements.txt
```

---

## 📌 Remarque Importante

- **Les tests doivent être exécutés dans l'ordre suivant** :
  1️⃣ Exécuter `test_E2E_personal_approval.py` en **env OK** pour créer un compte.
  2️⃣ Exécuter `test_personal_login_attempts.py` en **env KO**, car en KO, la création de compte est impossible et on doit réutiliser un compte créé en OK.
- Les identifiants créés sont **stockés dans `data/credentiels_par.json`**.
- **Si `credentiels_par.json` est vide, le test `test_personal_login_attempts.py` échouera avec une erreur `KeyError: 'email'`**.

---

## 🎯 Conclusion

Ce projet permet de tester de manière automatisée les principales fonctionnalités d'OpenCruise en utilisant **Playwright**, **pytest** et **Allure Reports**, tout en garantissant une architecture modulaire grâce au **Page Object Model (POM)**. L'intégration des fixtures assure une exécution fluide et optimisée des tests.

---
