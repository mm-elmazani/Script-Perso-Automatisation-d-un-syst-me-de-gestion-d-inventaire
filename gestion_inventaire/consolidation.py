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
