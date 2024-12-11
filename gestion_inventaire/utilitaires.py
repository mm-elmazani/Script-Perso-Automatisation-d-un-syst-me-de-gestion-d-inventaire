import os

def verifier_fichiers(dossier):
    """Vérifie que tous les fichiers dans un dossier sont des CSV."""
    fichiers_csv = [f for f in os.listdir(dossier) if f.endswith(".csv")]
    if not fichiers_csv:
        raise FileNotFoundError("Aucun fichier CSV trouvé dans le dossier spécifié.")
    return fichiers_csv

def log_erreur(message):
    """Enregistre un message d'erreur dans un fichier de log."""
    with open("erreurs.log", "a") as log_file:
        log_file.write(message + "\n")
