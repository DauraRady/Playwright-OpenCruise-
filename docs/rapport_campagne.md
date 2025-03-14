# 📝 Rapport de Campagne de Test – OpenCruise

## 📌 1. Synthèse (Executive Summary)

### **But du projet**

- Automatiser les tests Web d’OpenCruise (fonctionnalités critiques : création de compte, connexion, réservation, etc.) sur deux environnements :
  - https://opencruise-ok.sogeti-center.cloud (version « stable »)
  - https://opencruise-ko.sogeti-center.cloud (version « défectueuse »)
- Garantir que les fonctionnalités clés fonctionnent correctement en environnement « OK » et analyser les pannes dans l’environnement « KO » pour anticiper les erreurs.

### **Valeur ajoutée**

- Diminuer le temps de test manuel sur les parcours critiques (création de compte, connexion).
- Réduire le risque de régressions via des tests automatisés exécutés régulièrement (CI/CD).
- Documenter et tracer les anomalies détectées (déclaration d’anomalies).

### 🎯 **Objectif des tests**

Cette campagne de test vise à **vérifier les fonctionnalités critiques** d'OpenCruise, notamment la **création de compte**, l'**approbation**, la **connexion** et le **blocage de compte après tentatives infructueuses**, en se concentrant sur les **cas passants**.

### 📊 **Résumé des résultats**

- **Nombre total de cas de test** : 15
- **Nombre de cas testés** : 3
  - **Cas passants testés** : 3/15 (20%)
  - **Cas non passants testés** : 0/15 (0%)
- **Nombre total de fonctionnalités** : 5
  - **Fonctionnalités couvertes** : 3/5 (60%)
- **Succès (Pass)** : 3
- **Échecs (Fail)** : 0
- **Problèmes critiques identifiés** :
  1. **Création de compte professionnel échouée en environnement KO**
  2. **Fonctionnalité d'ajout d'un deuxième représentant indisponible en environnement KO**

---

## 🖥️ 2. Contexte du Test

### 🔹 **Projet testé**

- **Application** : OpenCruise
- **Modules testés** : Création de compte, approbation de compte, connexion, blocage de compte

### 📅 **Date et heure d’exécution**

- **Début** : 12 mars 2025, 09h30
- **Fin** : 12 mars 2025, 10h45

### ⚙️ **Environnement technique**

- **Systèmes d’exploitation** : Windows 11
- **Navigateur** : Google Chrome 121.0
- **Version de l’application** : V2.6

### 🛠 **Méthode et outils utilisés**

- **Automatisation** : Playwright + pytest
- **CI/CD** : GitHub Actions
- **Gestion des tests** : Documentation sur Git

---

## ✅ 3. Résultats des Tests et Analyse des anomalies

### 📋 **Tableau récapitulatif**

| **ID Test** | **Description** | **Environnement OK** | **Environnement KO** | **Sévérité** || ----------- | -------------------------------------------------------------- | -------------------- | ----------------------------------- |------------ |
| **T001** | Création et approbation d’un compte pro + connexion | ✅ Pass | ❌ Fail (compte non créé) | **Critique** |
| **T002** | Création et approbation d’un compte particulier + connexion | ✅ Pass | ❌ Fail (compte non créé) | **Critique** |
| **T003** | Connexion après 5 tentatives infructueuses + blocage de compte | ✅ Pass | N/A (impossible de créer un compte) | **Mineur** |

📌 **Logs et captures d’écran disponibles dans GitHub Actions (lien interne).**

---

## 📈 4. Analyse des Anomalies

## 🔴 Anomalie 1 : Création de compte impossible en environnement KO

- **Impact** : Les utilisateurs ne peuvent pas s'inscrire, bloquant l'accès à la plateforme.
- **Cause probable** : Échec de validation côté serveur.
- **Reproduction** :
  1.
  2. Cliquer sur "Créer un compte".
- **Résultat attendu** : Le compte est créé et validé.
- **Résultat obtenu** : Aucun compte créé.
- **Action recommandée** : Analyse des logs backend.

📸 **Screenshot** :
![Erreur Création de Compte](<../Impossible_de_créer_un compte_envKO.png>)

---

## 🔴 Anomalie 2 : Impossibilité d'ajouter un deuxième représentant en KO

- **Impact** : Limitation pour les entreprises qui nécessitent plusieurs représentants.
- **Cause probable** : Fonctionnalité absente ou désactivée en KO.
- **Reproduction** :
  1. Accéder à la page d'inscription.
  2. Remplir les champs obligatoires.
  3. Tenter d’ajouter un deuxième représentant.
- **Résultat attendu** : L’ajout du représentant est possible.
- **Résultat obtenu** : Aucune option pour ajouter un représentant.
- **Action recommandée** : Vérification de l’implémentation et activation de la fonctionnalité.

📸 **Screenshot** :

![Erreur Ajout Représentant](<../Pas de deuxime représentant pro.png>)

## 🎯 5. Justification des Fonctionnalités Automatisées

### **Pourquoi ces fonctionnalités ont été automatisées ?**

1. **Impact direct sur l’utilisateur final** : La connexion et la création de compte sont des fonctionnalités essentielles pour l’expérience utilisateur et impactent directement la conversion.
2. **Sécurité et conformité** : La gestion des connexions erronées et du blocage de compte est critique pour éviter les failles de sécurité.
3. **Réduction des coûts et délais** : Ces fonctionnalités nécessitent des tests fréquents ; les automatiser permet un gain de temps significatif.

### **Pourquoi d'autres fonctionnalités n’ont pas été automatisées ?**

- **Réservation** : Scénarios trop variés et dépendants de plusieurs conditions externes.
- **Tests exploratoires** : Certains cas nécessitent encore une validation humaine avant d’être automatisés.

---

## 🔧 6. Conception des Tests

### 🛠 **Méthodologie utilisée**

- **Tests basés sur les risques (Risk-Based Testing - ISTQB)** : Les fonctionnalités critiques ont été priorisées pour minimiser les risques d’interruption de service. L’impact en termes de business est majeur, car un échec sur l’inscription ou la connexion empêche l’accès au service, ce qui réduit la rétention utilisateur et impacte directement les revenus.

---

## 🏁 7. Conclusion et Recommandations

### 🚀 **Actions correctives immédiates**

1. **Corriger la création de compte en KO** 📌 **(Bloquant)**
2. **Activer la fonctionnalité d’ajout d’un deuxième représentant** 🚨 **(Non conforme à la spec)**

### 🔍 **Prochaines étapes**

- Ajouter **les cas non passants** aux tests.
- Étendre l’automatisation aux **tests UI et réservation**.
- Renforcer la **surveillance CI/CD** pour détecter les régressions.

---
