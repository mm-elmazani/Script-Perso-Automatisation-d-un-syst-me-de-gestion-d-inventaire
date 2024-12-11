import pandas as pd
import os

# Génération de plusieurs fichiers CSV avec différents thèmes de produits
themes_data = {
    "alimentation.csv": {
        "Produit": ["Pomme", "Banane", "Lait", "Pain", "Œufs"],
        "Quantité": [100, 150, 50, 80, 60],
        "Prix_Unitaire": [1.0, 0.8, 1.5, 2.0, 0.2],
        "Catégorie": ["Alimentation", "Alimentation", "Alimentation", "Alimentation", "Alimentation"],
    },
    "electronique.csv": {
        "Produit": ["Téléphone", "Tablette", "Ordinateur", "Écouteurs", "Clavier"],
        "Quantité": [10, 15, 7, 50, 30],
        "Prix_Unitaire": [500.0, 300.0, 1200.0, 50.0, 70.0],
        "Catégorie": ["Électronique", "Électronique", "Électronique", "Électronique", "Électronique"],
    },
    "meubles.csv": {
        "Produit": ["Chaise", "Table", "Armoire", "Lit", "Canapé"],
        "Quantité": [20, 10, 5, 7, 3],
        "Prix_Unitaire": [50.0, 120.0, 200.0, 500.0, 700.0],
        "Catégorie": ["Meubles", "Meubles", "Meubles", "Meubles", "Meubles"],
    },
    "vetements.csv": {
        "Produit": ["T-shirt", "Jeans", "Veste", "Chaussures", "Robe"],
        "Quantité": [50, 30, 20, 25, 10],
        "Prix_Unitaire": [20.0, 40.0, 60.0, 80.0, 100.0],
        "Catégorie": ["Vêtements", "Vêtements", "Vêtements", "Vêtements", "Vêtements"],
    },
    "bazar.csv": {
        "Produit": ["Lampe", "Cahier", "Stylo", "Ciseaux", "Colle"],
        "Quantité": [15, 40, 100, 25, 30],
        "Prix_Unitaire": [15.0, 2.0, 0.5, 3.0, 1.5],
        "Catégorie": ["Bazar", "Bazar", "Bazar", "Bazar", "Bazar"],
    },
}

output_dir = r"C:\Users\momoe\OneDrive - EPHEC asbl\BAC 2 - Q1\Q1 - Dev Info\4 - devoir\Scipt-perso\test_data"
os.makedirs(output_dir, exist_ok=True)

generated_files = []
for filename, data in themes_data.items():
    file_path = os.path.join(output_dir, filename)
    pd.DataFrame(data).to_csv(file_path, index=False)
    generated_files.append(file_path)

generated_files
