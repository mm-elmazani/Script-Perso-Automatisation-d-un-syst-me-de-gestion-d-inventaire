import pandas as pd
import os

class Consolidateur:
    def __init__(self):
        """Initialise une instance de Consolidateur avec un DataFrame vide."""
        self.data = pd.DataFrame()

    def charger_fichiers(self, dossier):
        """
        Charge et fusionne les fichiers CSV présents dans un dossier.

        Args:
            dossier (str): Chemin du dossier contenant les fichiers CSV.

        Returns:
            None: Fusionne les fichiers dans l'attribut `self.data`.
        """
        for fichier in os.listdir(dossier):
            if fichier.endswith('.csv'):
                chemin = os.path.join(dossier, fichier)
                try:
                    df = pd.read_csv(chemin)
                    self.data = pd.concat([self.data, df], ignore_index=True)
                except Exception as e:
                    print(f"Erreur lors du chargement de {fichier}: {e}")

    def nettoyer_donnees(self):
        """
        Nettoie les données consolidées :
        - Supprime les doublons.
        - Supprime les lignes avec des valeurs manquantes.
        """
        self.data.drop_duplicates(inplace=True)
        self.data.dropna(inplace=True)

    def sauvegarder(self, chemin):
        """
        Sauvegarde les données consolidées dans un fichier CSV.

        Args:
            chemin (str): Chemin du fichier de sortie.
        """
        self.data.to_csv(chemin, index=False)
        print(f"Données consolidées sauvegardées dans {chemin}")
