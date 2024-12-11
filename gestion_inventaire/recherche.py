class Recherche:
    def __init__(self, data):
        self.data = data

    def par_critere(self, **kwargs):
        resultat = self.data
        for cle, valeur in kwargs.items():
            if cle in self.data.columns:
                resultat = resultat[resultat[cle] == valeur]
        return resultat
