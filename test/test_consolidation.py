import pandas as pd
from gestion_inventaire.consolidation import Consolidateur

def test_consolidation():
    # Préparation des fichiers de test
    dossier_test = "test_data"
    
    # Création d'un objet Consolidateur
    consolidateur = Consolidateur()
    consolidateur.charger_fichiers(dossier_test)
    
    # Vérifications
    assert not consolidateur.data.empty, "Le DataFrame consolidé est vide."
    assert consolidateur.data.duplicated().sum() == 0, "Il reste des doublons dans les données."
    assert consolidateur.data.isnull().sum().sum() == 0, "Il y a encore des valeurs manquantes."
