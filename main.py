import os
import pandas as pd
from gestion_inventaire.consolidation import Consolidateur
from gestion_inventaire.recherche import Recherche
from gestion_inventaire.generation_rapport import Rapport

# Chemins par défaut
CHEMIN_PAR_DEFAUT = r"C:\Users\momoe\OneDrive - EPHEC asbl\BAC 2 - Q1\Q1 - Dev Info\4 - devoir\Scipt-perso\test_data"
DOSSIER_RAPPORT = r"C:\Users\momoe\OneDrive - EPHEC asbl\BAC 2 - Q1\Q1 - Dev Info\4 - devoir\Scipt-perso\outputs_rapport"

# Vérifier que le dossier de sortie existe, sinon le créer


def creer_dossier_si_absent(chemin):
    """
    Crée un dossier s'il n'existe pas déjà.
    """
    if not os.path.exists(chemin):
        os.makedirs(chemin)

creer_dossier_si_absent(DOSSIER_RAPPORT)

def afficher_menu():
    """
    Affiche le menu principal.
    """
    print("\n--- Menu Principal ---")
    print("1. Charger les fichiers CSV")
    print("2. Rechercher des informations")
    print("3. Générer un rapport")
    print("4. Quitter")
    choix = input("Entrez votre choix : ")
    return choix

def main():
    """
    Point d'entrée principal de l'application.
    """
    consolidateur = Consolidateur()
    donnees_chargees = False

    while True:
        choix = afficher_menu()

        if choix == "1":
            # Utiliser le chemin par défaut
            dossier = CHEMIN_PAR_DEFAUT
            print(f"Chemin par défaut utilisé : {dossier}")

            if not os.path.isdir(dossier):
                print("Le chemin spécifié est invalide.")
                continue

            try:
                consolidateur.charger_fichiers(dossier)
                consolidateur.nettoyer_donnees()
                print("Les fichiers ont été chargés et consolidés avec succès.")
                donnees_chargees = True

                 # Sauvegarder les données consolidées
                chemin_consolidation = os.path.join(DOSSIER_RAPPORT, "fichier_consolide.csv")
                consolidateur.sauvegarder(chemin_consolidation)

            except Exception as e:
                print(f"Erreur lors du chargement des fichiers : {e}")

        elif choix == "2":
            if not donnees_chargees:
                print("Veuillez d'abord charger les fichiers CSV (Option 1).")
                continue

            recherche = Recherche(consolidateur.data)
            print("\n--- Options de Recherche ---")
            print("1. Recherche par produit")
            print("2. Recherche par catégorie")
            print("3. Recherche par plage de prix")
            critere = input("Entrez votre choix : ")

            if critere == "1":
                produit = input("Entrez le nom du produit : ")
                resultats = recherche.par_produit(produit)
            elif critere == "2":
                categorie = input("Entrez le nom de la catégorie : ")
                resultats = recherche.par_categorie(categorie)
            elif critere == "3":
                try:
                    prix_min = float(input("Entrez le prix minimum : "))
                    prix_max = float(input("Entrez le prix maximum : "))
                    resultats = recherche.par_prix(prix_min, prix_max)
                except ValueError:
                    print("Les valeurs de prix doivent être des nombres.")
                    continue
            else:
                print("Option invalide.")
                continue

            if resultats.empty:
                print("Aucun résultat trouvé.")
            else:
                print("\nRésultats de la recherche :")
                print(resultats)

        elif choix == "3":
            if not donnees_chargees:
                print("Veuillez d'abord charger les fichiers CSV (Option 1).")
                continue

            chemin_rapport = os.path.join(DOSSIER_RAPPORT, "rapport_inventaire.csv")
            try:
                rapport = Rapport(consolidateur.data)
                rapport.generer_csv(chemin_rapport)
            except Exception as e:
                print(f"Erreur lors de la génération du rapport : {e}")

        elif choix == "4":
            print("Merci d'avoir utilisé l'application. Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
