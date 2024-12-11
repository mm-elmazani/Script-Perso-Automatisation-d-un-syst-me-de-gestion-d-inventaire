import unittest
import pandas as pd
import os
from gestion_inventaire.generation_rapport import Rapport

class TestRapport(unittest.TestCase):
    def setUp(self):
        """
        Configure les données pour les tests.
        """
        data = {
            "Produit": ["A", "B", "C", "D"],
            "Quantité": [10, 5, 8, 12],
            "Prix_Unitaire": [100, 50, 75, 150],
            "Catégorie": ["Cat1", "Cat1", "Cat2", "Cat3"]
        }
        self.data = pd.DataFrame(data)
        self.rapport = Rapport(self.data)
        self.output_file = "test_rapport.csv"

    def tearDown(self):
        """
        Supprime les fichiers après chaque test.
        """
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generer_csv(self):
        """
        Vérifie que le rapport est généré correctement en CSV.
        """
        self.rapport.generer_csv(self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

if __name__ == "__main__":
    unittest.main()
