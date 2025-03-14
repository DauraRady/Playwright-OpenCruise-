# 🚨 Déclaration des Anomalies – OpenCruise

## 📌 Objectif

Ce document liste les **anomalies détectées** lors des tests et leur **impact métier**.

## 🔴 Anomalie 1 : Création de compte impossible en environnement KO

- **Impact** : Les utilisateurs ne peuvent pas s'inscrire, bloquant l'accès à la plateforme.
- **Cause probable** : Échec de validation côté serveur.
- **Reproduction** :
  1. Accéder à la page d'inscription.
  2. Remplir les champs obligatoires.
  3. Cliquer sur "Créer un compte".
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

📌 **Ces anomalies sont documentées dans le [Rapport de Campagne](./rapport_campagne.md).**
