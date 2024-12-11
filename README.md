# Gestion d'Inventaire - Projet Python

Ce projet est une application de gestion d'inventaire permettant de :
- Charger et consolider des fichiers CSV contenant des informations sur les produits.
- Effectuer des recherches avancées dans l'inventaire (par produit, catégorie, plage de prix, etc.).
- Générer des rapports consolidés au format CSV.

## Structure du Projet

### Dossiers et Fichiers

```
projet/
├── gestion_inventaire/
│   ├── __init__.py               # Initialisation du package
│   ├── consolidation.py          # Gestion de la consolidation des fichiers CSV
│   ├── recherche.py              # Module de recherche dans les données consolidées
│   ├── generation_rapport.py     # Génération de rapports consolidés
├── tests/
│   ├── __init__.py               # Initialisation du package de tests
│   ├── test_consolidation.py     # Tests pour le module consolidation
│   ├── test_recherche.py         # Tests pour le module recherche
│   ├── test_generation_rapport.py# Tests pour la génération de rapports
├── main.py                       # Point d'entrée principal de l'application
├── README.md                     # Documentation du projet
├── test_data/                    # Dossier contenant les fichiers CSV de test
├── outputs_rapport/              # Dossier pour les rapports générés
```

### Modules

- **`consolidation.py`** :
  - Fusionne les fichiers CSV provenant d'un dossier.
  - Nettoie les données en supprimant les doublons et les valeurs manquantes.
  - Permet la sauvegarde des données consolidées dans un fichier CSV.

- **`recherche.py`** :
  - Recherche de produits par nom, catégorie ou plage de prix.
  - Supporte des recherches multicritères dynamiques.

- **`generation_rapport.py`** :
  - Génère des rapports statistiques par catégorie (quantité totale et valeur totale).
  - Produit les rapports au format CSV.

- **`tests/`** :
  - Contient les tests unitaires pour valider chaque module.

---

## Installation

### Pré-requis

1. **Python 3.8 ou supérieur**
2. **pip** (pour gérer les dépendances)
3. **Bibliothèques Python nécessaires** :

```bash
pip install pandas fpdf
```

---

## Utilisation

1. **Lancer l'application** :

Exécutez le fichier principal depuis la ligne de commande :

```bash
python main.py
```

2. **Options disponibles dans le menu** :
   - Charger des fichiers CSV.
   - Rechercher des informations dans l'inventaire.
   - Générer un rapport consolidé.

3. **Fichiers de test** :
   Placez les fichiers CSV dans le dossier `test_data` ou spécifiez leur chemin lors de l'utilisation de l'application.

4. **Rapports générés** :
   Les rapports consolidés seront sauvegardés dans le dossier `outputs_rapport/`.

---

## Tests Unitaires

Pour exécuter les tests unitaires et vérifier les modules :

```bash
python -m unittest discover -s tests -p "test_*.py"
```

---

## Fonctionnalités Implémentées

1. **Consolidation des Fichiers CSV** :
   - Chargement et fusion des fichiers CSV d'un dossier donné.
   - Nettoyage des données (suppression des doublons et des valeurs manquantes).

2. **Recherche dans les Données** :
   - Recherche par produit, catégorie ou plage de prix.
   - Recherche multicritères.

3. **Génération de Rapports** :
   - Rapports par catégorie avec des statistiques (quantité totale, valeur totale).
   - Export des rapports au format CSV.

---

## Structure des Données

Chaque fichier CSV doit avoir les colonnes suivantes :

- **Produit** : Nom du produit.
- **Quantité** : Quantité en stock.
- **Prix_Unitaire** : Prix par unité.
- **Catégorie** : Catégorie du produit.

Exemple :

| Produit     | Quantité | Prix_Unitaire | Catégorie     |
|-------------|----------|---------------|---------------|
| Pomme       | 100      | 1.0           | Alimentation  |
| Téléphone   | 10       | 500.0         | Électronique  |

---

## Auteurs

- Étudiant : [Mohamed Mokhtar El Mazani]
- Projet pour le cours de programmation Python.
