# 📝 Conception des Tests – OpenCruise

## 🎯 Objectifs des Tests

L’objectif principal des tests est de **vérifier les fonctionnalités critiques** de la plateforme OpenCruise afin de garantir :

- La fiabilité des parcours utilisateurs (création de compte, connexion, gestion des erreurs).
- La **détection rapide des anomalies** en environnement KO.
- La réduction du temps de test manuel grâce à l’automatisation.

## 📌 Stratégie de Test

Nous avons adopté une **approche basée sur les risques** (Risk-Based Testing - RBT) en nous concentrant sur :

🔹 **Les fonctionnalités critiques** pour l’utilisateur :

- Inscription et approbation de compte.
- Connexion et sécurité des authentifications.
- Blocage des comptes après plusieurs tentatives infructueuses.

🔹 **Les scénarios à forte valeur métier** :

- **Parcours utilisateur nominal** : Vérifier que les actions principales fonctionnent sans erreur.
- **Cas limites et erreurs** : Tester les réactions de l’application en cas d’entrée invalide ou de panne.

🔹 **Environnements de Test** :

- **OK** (Stable) : Valider que tout fonctionne normalement.
- **KO** (Défectueux) : Identifier et documenter les anomalies.

## 🏗️ Types de Tests

| Type de Test            | Objectif                                                                              |
| ----------------------- | ------------------------------------------------------------------------------------- |
| **Tests Fonctionnels**  | Vérifier que les fonctionnalités répondent aux exigences                              |
| **Tests de Sécurité**   | Assurer que les failles comme les accès non autorisés sont bloquées                   |
| **Tests de Régression** | Vérifier que les nouvelles mises à jour ne cassent pas les fonctionnalités existantes |

## 📌 Scénarios de Test (E2E)

Les scénarios détaillés des tests sont disponibles dans le fichier **`rapport de campagne.md`**.

### 🔹 **1. Test E2E Personal Approval**

✅ Accéder à la page d'inscription.
✅ Remplir le formulaire avec un email généré.
✅ Soumettre la création de compte.
✅ Vérifier la redirection vers la page de connexion.
✅ Connexion en tant qu'admin.
✅ Approuver le compte depuis l'interface admin.
✅ Vérifier que l'utilisateur peut se connecter après approbation.
✅ **Stockage des identifiants dans `credentiels_par.json` pour réutilisation.**

### 🔹 **2. Test E2E Professional Approval**

✅ Accéder à la page d'inscription entreprise.
✅ Remplir les informations nécessaires.
✅ Soumettre la création de compte.
✅ Vérifier la redirection vers la page de connexion.
✅ Connexion en tant qu'admin.
✅ Approuver le compte depuis l'interface admin.
✅ Vérifier que l'utilisateur professionnel peut se connecter après approbation.

### 🔹 **3. Test E2E Login Attempts (Blocage après 5 échecs)**

✅ Accéder à la page de connexion.
✅ Entrer des identifiants incorrects 5 fois.
✅ Vérifier l'affichage du message d'erreur.
✅ À la 6ᵉ tentative, tenter avec le bon mot de passe.
✅ Vérifier que l'utilisateur est bloqué et ne peut plus se connecter.
✅ **Utilisation des identifiants stockés dans `credentiels_par.json` (créés en env OK).**

---

## 🛠️ Outils Utilisés

- **Playwright** 🎭 → Automatisation UI.
- **pytest** 🧪 → Framework d’exécution des tests.
- **GitHub Actions** 🔄 → Intégration continue et exécution automatique.
