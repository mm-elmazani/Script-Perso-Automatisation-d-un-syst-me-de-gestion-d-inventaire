
# Plan pour réaliser et valider le projet Python

## **1. Étape de préparation**

### 1.1. Créer et configurer l’environnement :
1. Créer un environnement virtuel :
   ```bash
   python -m venv env
   source env/bin/activate
   ```
2. Installer les dépendances nécessaires :
   ```bash
   pip install pandas matplotlib fpdf pytest
   pip freeze > requirements.txt
   ```
3. Configurer un linter dans votre IDE (par exemple, `flake8` pour vérifier la conformité PEP8).

### 1.2. Initialiser le projet avec Git :
1. Initialiser un repository Git local :
   ```bash
   git init
   ```
2. Créer un fichier `.gitignore` pour exclure les fichiers inutiles :
   ```plaintext
   env/
   __pycache__/
   *.pyc
   *.log
   ```
3. Configurer un repository GitHub et le connecter :
   ```bash
   git remote add origin <URL_du_repository>
   ```

### 1.3. Organiser les fichiers du projet :
Structure de base :
```plaintext
gestion_inventaire/
├── consolidation.py
├── recherche.py
├── generation_rapport.py
├── utilitaires.py
tests/
├── test_consolidation.py
├── test_recherche.py
├── test_generation_rapport.py
main.py
requirements.txt
README.md
.gitignore
```

---

## **2. Développement du programme**

### 2.1. Module de consolidation des fichiers CSV (`consolidation.py`)
- Charger et fusionner plusieurs fichiers CSV.
- Nettoyer les données (gestion des colonnes manquantes, doublons).
- Générer un DataFrame consolidé.

**Exemple :**
```python
import pandas as pd
import os

class Consolidateur:
    def __init__(self):
        self.data = pd.DataFrame()

    def charger_fichiers(self, dossier):
        for fichier in os.listdir(dossier):
            if fichier.endswith('.csv'):
                chemin = os.path.join(dossier, fichier)
                df = pd.read_csv(chemin)
                self.data = pd.concat([self.data, df], ignore_index=True)

    def nettoyer_donnees(self):
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplace=True)
```

---

### 2.2. Module de recherche (`recherche.py`)
- Rechercher des produits selon plusieurs critères (par produit, catégorie, plage de prix).
- Gérer des recherches multicritères.

**Exemple :**
```python
class Recherche:
    def __init__(self, data):
        self.data = data

    def par_critere(self, **kwargs):
        resultat = self.data
        for cle, valeur in kwargs.items():
            if cle in self.data.columns:
                resultat = resultat[resultat[cle] == valeur]
        return resultat
```

---

### 2.3. Module de génération de rapports (`generation_rapport.py`)
- Générer des rapports sous forme de fichiers CSV et PDF.
- Inclure des informations comme :
  - Quantité totale par catégorie.
  - Valeur totale du stock.
  - Produits en stock critique (quantité < seuil).

**Exemple :**
```python
from fpdf import FPDF

class Rapport:
    def __init__(self, data):
        self.data = data

    def generer_pdf(self, chemin):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Rapport d'Inventaire", ln=True, align="C")
        # Ajouter des données au PDF...
        pdf.output(chemin)
```

---

### 2.4. Menu interactif (`main.py`)
- Fournir une interface utilisateur pour :
  - Charger des fichiers.
  - Rechercher des produits.
  - Générer des rapports.

**Exemple :**
```python
def menu():
    print("1. Charger des fichiers")
    print("2. Rechercher un produit")
    print("3. Générer un rapport")
    print("4. Quitter")
    choix = input("Entrez votre choix : ")
    return choix
```

---

## **3. Validation (Tests unitaires)**

### 3.1. Écrire des tests unitaires :
- Utiliser `pytest` pour tester chaque module.
- Exemple de test pour `consolidation.py` :
```python
import pandas as pd
from gestion_inventaire.consolidation import Consolidateur

def test_consolidation():
    consolidateur = Consolidateur()
    consolidateur.charger_fichiers("test_data")
    assert not consolidateur.data.empty, "La consolidation a échoué : DataFrame vide."
```

### 3.2. Exécuter les tests :
- Lancer les tests avec la commande :
  ```bash
  pytest tests/
  ```

---

## **4. Documentation et vidéo**

### 4.1. Rédiger un fichier `README.md` :
- Inclure :
  - Introduction.
  - Installation et utilisation.
  - Description des fonctionnalités.
  - Instructions pour exécuter les tests.

### 4.2. Wiki GitHub :
- Ajouter des pages pour :
  - Les fonctionnalités SMART.
  - L’utilisation des outils (Git, pytest, etc.).

### 4.3. Vidéo démonstrative :
- Montrer :
  - Exécution du script.
  - Recherche d’un produit.
  - Génération d’un rapport.
  - Exécution des tests unitaires.

---

## **5. Suivi de la qualité du code**
- Utiliser un linter (par exemple `flake8`) pour vérifier :
  ```bash
  flake8 gestion_inventaire
  ```
- S’assurer que le code respecte la norme PEP8 :
  - Bonne indentation.
  - Noms de variables explicites.
  - Documentation des classes et fonctions.

---

## **6. Livraison**

### 6.1. Pousser le projet sur GitHub :
```bash
git add .
git commit -m "Version finale du projet"
git push
```

### 6.2. Inclure tous les livrables :
- Code source.
- Documentation (README.md + Wiki).
- Vidéo démonstrative.
