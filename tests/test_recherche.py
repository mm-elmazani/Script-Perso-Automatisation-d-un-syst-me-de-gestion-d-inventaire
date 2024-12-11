import unittest
import pandas as pd
from gestion_inventaire.recherche import Recherche

class TestRecherche(unittest.TestCase):
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
        self.recherche = Recherche(self.data)

    def test_par_produit(self):
        """
        Vérifie la recherche par produit.
        """
        result = self.recherche.par_produit("A")
        self.assertEqual(len(result), 1)
        self.assertEqual(result.iloc[0]["Produit"], "A")

    def test_par_categorie(self):
        """
        Vérifie la recherche par catégorie.
        """
        result = self.recherche.par_categorie("Cat1")
        self.assertEqual(len(result), 2)

    def test_par_prix(self):
        """
        Vérifie la recherche par plage de prix.
        """
        result = self.recherche.par_prix(50, 100)
        self.assertEqual(len(result), 3)

if __name__ == "__main__":
    unittest.main()
