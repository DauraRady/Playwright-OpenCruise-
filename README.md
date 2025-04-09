# 🏗️ Documentation du Projet de Tests Automatisés – OpenCruise

Bienvenue dans la documentation du projet d'automatisation des tests de **OpenCruise**. Ce projet utilise **Playwright** et **pytest** pour tester les fonctionnalités critiques.

📌 Cette documentation est divisée en plusieurs sections :

1. **[Conception des Tests](./docs/conception_tests.md)** 📝
2. **[Automatisation des Tests](./docs/automatisation_tests.md)** 🤖
3. **[Rapport de Campagne de Test](./docs/rapport_campagne.md)** 📊
4. **[Déclaration des Anomalies](./docs/declaration_anomalies.md)** 🛑

## 📂 Organisation des Fichiers

📦 PLAYWRIGHT_PYTHON_OPENCRUISE
├── data/ # Fichiers JSON de configuration
├── docs/ # Documentation projet & test
├── pages/ # Pages objets (Page Object Model)
├── tests/ # Cas de test automatisés Playwright
├── videos/ # Enregistrements vidéos des tests
├── .github/workflows/ # CI GitHub Actions
│ └── playwright.yml
├── requirements.txt # Dépendances Python
├── README.md

📁 `docs/` → Contient la documentation du projet.

- `conception_tests.md` → Décrit la méthodologie et la stratégie de test.
- `automatisation_tests.md` → Explique l’implémentation des tests automatisés.
- `rapport_campagne.md` → Contient les résultats des tests.
- `declaration_anomalies.md` → Liste les anomalies détectées et leur impact.

📁 `videos/` → Stocke les enregistrements des tests exécutés.

- `test_E2E_particulier.webm` → Démo du test de création de compte,approbation par l'admin et connexion.
- `test_E2E_professional.webm` → Démo du test de création de compte,approbation par l'admin et connexion.

📁 `screenshots/` → Contient des captures d’écran des anomalies.

- `Impossible_de_créer_uncompte_envKO.png`
- `Pas de deuxiéme représentant pro.png`

## 🎥 Intégration des Vidéos et Captures d’Écran

Dans chaque documentation spécifique (`rapport_campagne.md`, `declaration_anomalies.md`), les vidéos et images seront intégrées ainsi :

- **Images** :

![Impossible_de_créer_un compte_envKO](<Impossible_de_créer_un compte_envKO.png>)
![Pas de deuxiéme représentant pro](<Pas de deuxiéme représentant pro.png>)

- **Vidéos** :
  [E2E part](videos/test_E2E_particulier.webm)
  [E2E pro](videos/test_E2E_professional.webm)

📌 **Assurez-vous que les fichiers sont bien stockés dans les bons dossiers pour un affichage correct.**

---

🔁 Intégration Continue (CI) avec GitHub Actions
Ce projet utilise GitHub Actions pour automatiser les tests Playwright à chaque push ou pull request sur la branche main.

⚙️ Pipeline CI
Le fichier de configuration se trouve ici :

bash
Copier
Modifier
.github/workflows/playwright.yml
🔧 Que fait le pipeline ?
Installe Python + les dépendances

Installe les navigateurs Playwright

Exécute tous les tests dans tests/ via pytest

Génère un rapport HTML avec pytest-html

Uploade ce rapport dans les Artifacts GitHub

📤 Voir le rapport de test
Après chaque exécution, allez dans l’onglet Actions de GitHub :

Sélectionner le dernier workflow

Aller dans la section “Artifacts”

Télécharger report.html

🧪 Lancer les tests localement
bash

pip install -r requirements.txt
playwright install
pytest tests/ --html=report.html --self-contained-html
Le rapport sera généré dans le fichier report.html.

📌 **Naviguez vers les différentes sections via les liens ci-dessus pour explorer la documentation complète !** 🚀
