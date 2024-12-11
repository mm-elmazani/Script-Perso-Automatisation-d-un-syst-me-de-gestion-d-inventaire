class Recherche:
    def __init__(self, data):
        """
        Initialise une instance de Recherche.
        
        Args:
            data (DataFrame): Données consolidées sous forme de DataFrame.
        """
        self.data = data

    def par_produit(self, produit):
        """Recherche un produit spécifique."""
        return self.data[self.data["Produit"] == produit]

    def par_categorie(self, categorie):
        """Recherche tous les produits dans une catégorie donnée."""
        return self.data[self.data["Catégorie"] == categorie]

    def par_prix(self, prix_min, prix_max):
        """Recherche tous les produits dans une plage de prix."""
        return self.data[(self.data["Prix_Unitaire"] >= prix_min) & (self.data["Prix_Unitaire"] <= prix_max)]

    def multicritere(self, **kwargs):
        """
        Recherche des produits selon plusieurs critères.
        
        Args:
            kwargs: Critères de recherche (e.g., Produit, Catégorie, Quantité).
        
        Returns:
            DataFrame: Résultats de la recherche.
        """
        result = self.data
        for cle, valeur in kwargs.items():
            if cle in self.data.columns:
                result = result[result[cle] == valeur]
        return result
