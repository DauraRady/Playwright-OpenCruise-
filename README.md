# 🏗️ Documentation du Projet de Tests Automatisés – OpenCruise

Bienvenue dans la documentation du projet d'automatisation des tests de **OpenCruise**. Ce projet utilise **Playwright** et **pytest** pour tester les fonctionnalités critiques.

📌 Cette documentation est divisée en plusieurs sections :

1. **[Conception des Tests](./docs/conception_tests.md)** 📝
2. **[Automatisation des Tests](./docs/automatisation_tests.md)** 🤖
3. **[Rapport de Campagne de Test](./docs/rapport_campagne.md)** 📊
4. **[Déclaration des Anomalies](./docs/declaration_anomalies.md)** 🛑

## 📂 Organisation des Fichiers

📁 `docs/` → Contient la documentation du projet.

- `conception_tests.md` → Décrit la méthodologie et la stratégie de test.
- `automatisation_tests.md` → Explique l’implémentation des tests automatisés.
- `rapport_campagne.md` → Contient les résultats des tests.
- `declaration_anomalies.md` → Liste les anomalies détectées et leur impact.

📁 `videos/` → Stocke les enregistrements des tests exécutés.

- `test_demo.webm` → Démo du test de connexion.
- `test_blocage.webm` → Démo du test de blocage après 5 tentatives.

📁 `screenshots/` → Contient des captures d’écran des anomalies.

- `anomalie_creation_compte.png`
- `anomalie_connexion_bloquee.png`

## 🎥 Intégration des Vidéos et Captures d’Écran

Dans chaque documentation spécifique (`rapport_campagne.md`, `declaration_anomalies.md`), les vidéos et images seront intégrées ainsi :

- **Images** :
  ```markdown
  ![Création de compte KO](../screenshots/anomalie_creation_compte.png)
  ```
- **Vidéos** :
  ```markdown
  [🎥 Voir la vidéo du test de connexion](../videos/test_demo.webm)
  ```

📌 **Assurez-vous que les fichiers sont bien stockés dans les bons dossiers pour un affichage correct.**

---

📌 **Naviguez vers les différentes sections via les liens ci-dessus pour explorer la documentation complète !** 🚀
