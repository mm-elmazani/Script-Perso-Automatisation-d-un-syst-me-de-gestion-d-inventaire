import pandas as pd

class Rapport:
    def __init__(self, data):
        """
        Initialise une instance de Rapport.

        Args:
            data (DataFrame): Données consolidées sous forme de DataFrame.
        """
        self.data = data

    def generer_csv(self, chemin):
        """
        Génère un rapport CSV contenant les statistiques des données.

        Args:
            chemin (str): Chemin du fichier CSV à générer.
        """
        # Calculer les statistiques par catégorie
        stats = self.data.groupby("Catégorie").agg(
            Total_Quantité=("Quantité", "sum"),
            Valeur_Totale=("Prix_Unitaire", lambda x: (x * self.data.loc[x.index, "Quantité"]).sum())
        )

        # Calculer le total général
        total_general = stats.sum()
        total_general.name = "TOTAL"

        # Ajouter la ligne des totaux avec `pd.concat`
        stats = pd.concat([stats, pd.DataFrame([total_general])])

        # Sauvegarder les statistiques dans un fichier CSV
        stats.to_csv(chemin)
        print(f"Rapport CSV sauvegardé dans {chemin}")
