import unittest
import pandas as pd
import os
import shutil
from gestion_inventaire.consolidation import Consolidateur

class TestConsolidateur(unittest.TestCase):
    def setUp(self):
        """
        Configure les fichiers de test avant chaque test.
        """
        self.test_folder = "test_data"
        os.makedirs(self.test_folder, exist_ok=True)

        # Créer des fichiers CSV de test
        self.file_1 = os.path.join(self.test_folder, "test_file_1.csv")
        self.file_2 = os.path.join(self.test_folder, "test_file_2.csv")

        data_1 = {"Produit": ["A", "B", "C"], "Quantité": [10, 5, 8], "Prix_Unitaire": [100, 50, 75], "Catégorie": ["Cat1", "Cat1", "Cat2"]}
        data_2 = {"Produit": ["C", "D"], "Quantité": [3, 12], "Prix_Unitaire": [75, 150], "Catégorie": ["Cat2", "Cat3"]}

        pd.DataFrame(data_1).to_csv(self.file_1, index=False)
        pd.DataFrame(data_2).to_csv(self.file_2, index=False)

    def tearDown(self):
        """
        Supprime les fichiers et dossiers de test après chaque test.
        """
        for file in [self.file_1, self.file_2]:
            try:
                if os.path.exists(file):
                    os.remove(file)  # Supprime chaque fichier
            except Exception as e:
                print(f"Impossible de supprimer le fichier : {file}. Erreur : {e}")

        if os.path.exists(self.test_folder):
            try:
                shutil.rmtree(self.test_folder, ignore_errors=True)
            except Exception as e:
                print(f"Impossible de supprimer le dossier : {self.test_folder}. Erreur : {e}")



    def test_charger_fichiers(self):
        """
        Vérifie que les fichiers CSV sont correctement chargés.
        """
        consolidateur = Consolidateur()
        consolidateur.charger_fichiers(self.test_folder)

        # Vérifie que le DataFrame n'est pas vide
        self.assertFalse(consolidateur.data.empty)

        # Vérifie que le nombre de lignes est correct (les données créées dans setUp)
        print("Données consolidées :", consolidateur.data)
        self.assertEqual(len(consolidateur.data), 5)  # Attendez-vous à 5 lignes pour les données créées


    def test_nettoyer_donnees(self):
        """
        Vérifie que les doublons sont supprimés correctement.
        """
        consolidateur = Consolidateur()
        consolidateur.charger_fichiers(self.test_folder)

        # Ajouter des doublons artificiels
        consolidateur.data = pd.concat([consolidateur.data, consolidateur.data])

        # Debugging avant nettoyage
        print("Données avant nettoyage :", consolidateur.data)

        # Nettoyer les données
        consolidateur.nettoyer_donnees()

        # Debugging après nettoyage
        print("Données après nettoyage :", consolidateur.data)

        # Vérifiez que les doublons sont supprimés
        self.assertEqual(len(consolidateur.data), 5)  # Attendez-vous à 5 lignes pour les données uniques


    def test_sauvegarder(self):
        """
        Vérifie que les données consolidées sont correctement sauvegardées.
        """
        consolidateur = Consolidateur()
        consolidateur.charger_fichiers(self.test_folder)

        # Chemin pour le fichier sauvegardé
        output_file = "output_test.csv"
        consolidateur.sauvegarder(output_file)

        # Vérifie que le fichier est créé
        self.assertTrue(os.path.exists(output_file))

        # Supprime le fichier après le test
        os.remove(output_file)

    

if __name__ == "__main__":
    unittest.main()
