# 🧪 Conception des Tests – OpenCruise 

## 🎯 Objectifs des Tests

L’objectif principal des tests est de **vérifier les fonctionnalités critiques** de la plateforme OpenCruise afin de garantir :

- La fiabilité des parcours utilisateurs (création de compte, connexion, gestion des erreurs).
- La **détection rapide des anomalies** en environnement KO.
- La réduction du temps de test manuel grâce à l’automatisation.

---

## 🧠 Stratégie de Test

Approche **Risk-Based Testing (RBT)** ciblant :

- **Fonctionnalités critiques** : création, connexion, sécurité.
- **Parcours à forte valeur métier** : nominal, erreur, validation admin.
- **Double environnement** :
  - **OK** (stable) : validation comportement attendu.
  - **KO** (défectueux) : identification des failles.

---

## 🏗️ Types de Tests Réalisés

| Type de Test        | Objectif                                                  |
| ------------------- | --------------------------------------------------------- |
| Tests Fonctionnels  | Vérifier la conformité fonctionnelle de chaque parcours   |
| Tests de Sécurité   | Contrôler les tentatives de contournement ou d'injection  |
| Tests de Régression | Détecter les régressions sur des fonctionnalités validées |

---

## 📋 Scénarios de Test (structurés)

### 🔹 1. Création & Approbation de Compte Personnel

| ID | Titre | Objectif | Prérequis |  
Étapes | Données | Résultat attendu | Type |
| ---- | ---------------------------- | --------------------------------------------- | ------------------- | ------------------------------------- | ---------------------- | ------------------------------- | -------------- |
| TC01 | Création compte perso valide | Vérifier qu’un utilisateur peut créer un cpte | Aucun | Aller à inscription, remplir, valider | Email valide, mdp fort | Redirection vers login | ✅ Passant |
| TC02 | Email invalide | Vérifier la validation email | Aucun | Saisir email invalide, valider | test.com | Message « email invalide » | ❌ Non Passant |
| TC03 | Mdp faible | Contrôle sécurité | Aucun | Saisir mdp court, valider | abc | Message « mot de passe faible » | ❌ Non Passant |
| TC04 | Champs vides | Vérifier champs obligatoires | Aucun | Soumettre sans rien remplir | - | Messages d’erreur affichés | ❌ Non Passant |
| TC05 | Connexion sans approbation | Vérifier le blocage tant que non approuvé | Compte non approuvé | Connexion avec email/mdp | - | Message "compte non approuvé" | ❌ Non Passant |
| TC06 | Connexion après approbation | Valider l’accès après action admin | Compte approuvé | Connexion avec email/mdp | - | Connexion réussie | ✅ Passant |

---

### 🔹 2. Création & Approbation de Compte Professionnel

| ID   | Titre                      | Objectif                                 | Prérequis           | Étapes                                | Données                       | Résultat attendu                | Type           |
| ---- | -------------------------- | ---------------------------------------- | ------------------- | ------------------------------------- | ----------------------------- | ------------------------------- | -------------- |
| TC07 | Création compte pro valide | Créer un compte entreprise complet       | Aucun               | Aller à inscription, remplir, valider | Raison sociale + SIRET valide | Redirection vers login          | ✅ Passant     |
| TC08 | SIRET invalide             | Vérifier la validation du champ métier   | Aucun               | Remplir SIRET incorrect, valider      | 123456                        | Message « SIRET invalide »      | ❌ Non Passant |
| TC09 | Champs obligatoires vides  | Vérifier comportement sans saisie        | Aucun               | Soumettre vide                        | -                             | Erreurs sur chaque champ        | ❌ Non Passant |
| TC10 | Connexion sans validation  | Vérifier le blocage si pas encore validé | Compte non approuvé | Tentative de connexion                | -                             | Message « compte non approuvé » | ❌ Non Passant |
| TC11 | Connexion après validation | Valider le login après approbation       | Compte approuvé     | Connexion                             | -                             | Connexion autorisée             | ✅ Passant     |

---

### 🔹 3. Blocage après 5 Tentatives Échouées

| ID   | Titre                   | Objectif                            | Prérequis     | Étapes                           | Données       | Résultat attendu                  | Type           |
| ---- | ----------------------- | ----------------------------------- | ------------- | -------------------------------- | ------------- | --------------------------------- | -------------- |
| TC12 | Échec 5 fois            | Vérifier le blocage après 5 erreurs | Compte valide | Essayer mauvais mdp x5           | Mdp incorrect | Message erreur + blocage          | ✅ Passant     |
| TC13 | Tentative après blocage | Vérifier que le blocage persiste    | Compte bloqué | Connexion avec bon mdp           | Bon mdp       | Accès toujours bloqué             | ✅ Passant     |
| TC14 | Injection SQL           | Tester la sécurité de l’input       | Aucun         | Saisir `' OR 1=1--`              | SQL injection | Message générique                 | ❌ Non Passant |
| TC15 | Compte inexistant       | Gérer la tentative sur user inconnu | Aucun         | Connexion avec email fake        | fake@test.com | Message "identifiants incorrects" | ❌ Non Passant |
| TC16 | Reset après blocage     | Vérifier si le reset débloque       | Compte bloqué | Mot de passe oublié, nouveau mdp | -             | Connexion toujours bloquée        | ❌ Non Passant |

---

## 🔧 Outils & Environnement

- **Playwright** 🎭 : UI automation
- **pytest** 🧪 : Exécution des scénarios
- **GitHub Actions** 🔁 : Intégration continue
- **Environnements** : `OK` (stable) & `KO` (défectueux)

---

Souhaites-tu maintenant la version automatisée (pytest) ou un export Gherkin BDD ?
