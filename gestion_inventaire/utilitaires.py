import os

def verifier_fichiers(dossier):
    """
    Vérifie que tous les fichiers dans un dossier sont des fichiers CSV.

    Args:
        dossier (str): Chemin du dossier à vérifier.

    Returns:
        list: Liste des fichiers CSV trouvés dans le dossier.

    Raises:
        FileNotFoundError: Si aucun fichier CSV n'est trouvé.
    """
    fichiers_csv = [f for f in os.listdir(dossier) if f.endswith(".csv")]
    if not fichiers_csv:
        raise FileNotFoundError("Aucun fichier CSV trouvé dans le dossier spécifié.")
    return fichiers_csv

def log_erreur(message, chemin_log="erreurs.log"):
    """
    Enregistre un message d'erreur dans un fichier de log.

    Args:
        message (str): Message à enregistrer.
        chemin_log (str): Chemin du fichier de log (par défaut : "erreurs.log").
    """
    with open(chemin_log, "a") as fichier_log:
        fichier_log.write(message + "\n")

def creer_dossier_si_absent(chemin):
    """
    Crée un dossier si celui-ci n'existe pas déjà.

    Args:
        chemin (str): Chemin du dossier à créer.
    """
    if not os.path.exists(chemin):
        os.makedirs(chemin)
