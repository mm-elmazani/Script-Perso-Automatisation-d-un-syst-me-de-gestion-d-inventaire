import unittest
import pandas as pd
from gestion_inventaire.consolidation import Consolidateur
import os

class TestConsolidateur(unittest.TestCase):
    def setUp(self):
        """
        Configure les données et fichiers nécessaires avant chaque test.
        """
        # Crée un dossier temporaire pour les fichiers de test
        self.test_folder = "test_data"
        os.makedirs(self.test_folder, exist_ok=True)
        
        # Fichiers de test
        self.file_1 = os.path.join(self.test_folder, "test_file_1.csv")
        self.file_2 = os.path.join(self.test_folder, "test_file_2.csv")
        
        # Contenus des fichiers de test
        data_1 = {
            "Produit": ["Produit A", "Produit B", "Produit C"],
            "Quantité": [10, 5, 8],
            "Prix_Unitaire": [100, 50, 75],
            "Catégorie": ["Cat1", "Cat1", "Cat2"]
        }
        data_2 = {
            "Produit": ["Produit C", "Produit D"],
            "Quantité": [3, 12],
            "Prix_Unitaire": [75, 150],
            "Catégorie": ["Cat2", "Cat3"]
        }
        
        # Création des fichiers CSV
        pd.DataFrame(data_1).to_csv(self.file_1, index=False)
        pd.DataFrame(data_2).to_csv(self.file_2, index=False)
        
    def tearDown(self):
        """
        Nettoie les fichiers et dossiers après chaque test.
        """
        # Supprimer les fichiers de test
        for file in [self.file_1, self.file_2]:
            if os.path.exists(file):
                os.remove(file)
        
        # Supprimer le dossier
        if os.path.exists(self.test_folder):
            os.rmdir(self.test_folder)
        
    def test_charger_fichiers(self):
        """
        Teste la méthode `charger_fichiers` pour vérifier que les fichiers sont bien chargés.
        """
        consolidateur = Consolidateur()
        consolidateur.charger_fichiers(self.test_folder)
        
        # Vérifie que les données sont bien consolidées
        self.assertFalse(consolidateur.data.empty, "Les données consolidées sont vides.")
        self.assertEqual(len(consolidateur.data), 5, "Le nombre total de lignes n'est pas correct.")
        
    def test_nettoyer_donnees(self):
        """
        Teste la méthode `nettoyer_donnees` pour vérifier que les doublons sont supprimés.
        """
        consolidateur = Consolidateur()
        consolidateur.charger_fichiers(self.test_folder)
        
        # Ajouter des doublons artificiels
        consolidateur.data = pd.concat([consolidateur.data, consolidateur.data])
        self.assertGreater(len(consolidateur.data), 5, "Les doublons n'ont pas été ajoutés correctement.")
        
        # Nettoyage des données
        consolidateur.nettoyer_donnees()
        self.assertEqual(len(consolidateur.data), 5, "Les doublons n'ont pas été supprimés correctement.")
        
    def test_sauvegarder(self):
        """
        Teste la méthode `sauvegarder` pour vérifier que les données sont sauvegardées dans un fichier CSV.
        """
        consolidateur = Consolidateur()
        consolidateur.charger_fichiers(self.test_folder)
        
        # Sauvegarde des données
        output_file = "output_test.csv"
        consolidateur.sauvegarder(output_file)
        
        # Vérifie que le fichier a été créé
        self.assertTrue(os.path.exists(output_file), "Le fichier de sortie n'a pas été créé.")
        
        # Nettoyage
        if os.path.exists(output_file):
            os.remove(output_file)

if __name__ == "__main__":
    unittest.main()
