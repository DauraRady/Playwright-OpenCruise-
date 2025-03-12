Documentation d’automatisation – Open Cruise
1. Contexte et objectifs
But du projet
• Automatiser les tests Web d’Open Cruise (fonctionnalités critiques : création de compte, connexion, réservation, etc.) sur deux environnements : 
o opencruise-ok.sogeti-center.cloud (version « stable »)
o opencruise-ko.sogeti-center.cloud (version « défectueuse »)
• Garantir que les fonctionnalités clés fonctionnent correctement en environnement « OK » et analyser les pannes dans l’environnement « KO » pour anticiper les erreurs.
Valeur ajoutée
• Diminuer le temps de test manuel sur les parcours critiques (création de compte, connexion).
• Réduire le risque de régressions via des tests automatisés exécutés régulièrement (CI/CD).
• Documenter et tracer les anomalies détectées (déclaration d’anomalies).

2. Périmètre fonctionnel
Fonctionnalités testées
1. Création de compte (Particulier/Professionnel) : 
o Champs obligatoires, validation des formats, etc.
2. Connexion : 
o Gestion des rôles (Particulier, Pro, Admin).
o Blocage du compte après 5 tentatives infructueuses.
3. Réservation (à titre d’illustration dans la suite, si nécessaire) : 
o Sélection de la croisière et ajout au panier.
o Vérification du prix, application de promotions, etc.
Scénarios spécifiques à l’environnement KO
• Simulation de bugs (par exemple, service d’authentification en panne).
• Contrôle des messages d’erreur et de la robustesse du site.

3. Organisation du projet
Le projet Git est privé, nommé :

projet_tutore_sujet3_prenom_nom

Répertoires principaux :
• doc/ : contient la documentation au format Markdown. 
o doc/README.md : contient l’architecture générale, la configuration de l’environnement, etc.
o doc/TEST_PLAN.md : décrit le plan de test (cas de tests à automatiser, priorités, etc.).
o doc/TEST_REPORT.md : rapport de campagne de tests, anomalies remontées, etc.
• tests/ : contient le code source des tests automatisés. 
o pages/ (optionnel) : implémente le Page Object Model (POM) pour chaque page Open Cruise (LoginPage, SignUpPage, etc.).
o conftest.py / fixtures/ : configuration Playwright, paramètres d’environnement, etc.
• README.md (racine) : une synthèse rapide pour exécuter les tests.

4. Choix technologiques
• Langage & Framework : Python + Playwright
o Pourquoi ? 
• Playwright gère plusieurs navigateurs (Chromium, Firefox, WebKit).
• Facilité d’écriture et de maintenance du code de test en Python.
• Bonne intégration continue possible (GitHub Actions, GitLab CI…).
• Structure & Maintenance :
o Page Object Model (POM) : chaque fonctionnalité du site a sa classe dédiée, ce qui rend le code de test plus lisible et évolutif.
o Fichiers de configuration : séparation claire des URLs et credentials selon l’environnement (OK ou KO).

5. Méthodologie de tests
5.1 Sélection des cas de tests
• Cas critiques : 
1. Création de compte (happy path et cas d’erreur).
  Première interaction des utilisateurs avec l’application → Si la création de compte ne fonctionne pas, aucun utilisateur ne peut utiliser la plateforme. 
  Deux types de comptes → L’application gère des profils différents (Pro vs Particulier), donc il faut tester que le formulaire s’adapte bien. 
  Vérifier les règles métiers et validations → Test des erreurs (ex: email déjà utilisé, mot de passe trop court, etc.).
2. Connexion (profil Particulier, Pro, Admin, gestion du blocage).
  Point d’entrée obligatoire → Sans connexion, l’admin ne peut pas gérer l’application. 
  Sécurité → On vérifie que seul un admin peut se connecter et voir certaines pages. 
  Test rapide et facile à exécuter en continu → Vérifier si l’application est disponible dès le début.

3. (Optionnel) Parcours de réservation, car il est central pour le business.
• Cas négatifs (environnement KO) : 
o Service d’auth down, tests de validations, etc.
o Vérification du comportement quand les réponses serveurs sont incorrectes.
5.2 Données de test
• Jeux de données : 
o Fichiers JSON/YAML/CSV pour stocker emails, mots de passe, SIRET, etc.
o Variables d’environnement pour éviter de committer les credentials sur Git.
5.3 Déroulement d’une exécution
1. Installation : pip install -r requirements.txt
2. Configuration : Choix de l’environnement via un flag ou variable (ex. ENV=ok ou ENV=ko).
3. Lancement : pytest --headed --env=ok ou --env=ko (selon la config).
4. Reporting : Génération d’un rapport HTML/Allure/Playwright.

6. Intégration continue & rapport de tests
1. Pipeline CI
o Exécution automatique des tests sur chaque commit/pull request.
o Deux jobs (un pour l’ENV=ok et un pour l’ENV=ko).
2. Rapport d’exécution
o doc/TEST_REPORT.md : inclut le nombre de tests passés/échoués, la liste des anomalies trouvées.
o S’il y a des échecs sur l’environnement KO, vérifier si ce sont des bugs « attendus » ou de nouveaux bugs.
3. Déclaration d’anomalies
o Création d’issues sur le tracker (GitLab/GitHub) avec : 
• Description du scénario.
• Steps to reproduce.
• Comportement attendu vs. observé.
• Logs et captures d’écran (Playwright gère la prise de screenshots en cas d’erreur).

7. Recommandations et points clés
• Ne jamais committer les mots de passe ou accès administrateur. Utilise des variables d’environnement ou un gestionnaire de secrets.
• Mettre à jour la doc dès qu’un nouveau test est ajouté ou qu’une spec change.
• Analyser régulièrement la pertinence des cas de tests pour éviter de maintenir des scripts obsolètes.

8. Conclusion
La documentation de l’automatisation doit donner une vision claire :
• Des objectifs (quoi tester et pourquoi).
• De la méthode (architecture, outillage).
• Des résultats attendus (comment lire et interpréter les rapports).
• De la maintenance future (comment ajouter ou modifier des tests, où trouver les infos).
En suivant ce guide, toute l’équipe peut comprendre l’intérêt et le fonctionnement de l’automatisation : on sait où regarder, comment l’exécuter et pourquoi on l’a mise en place.

