class Cargaison:
    type_cargaison = "Cargaison"

    def __init__(self, distance, express=False):
        self.distance = distance
        self.express = express
        self.produits = []

    def get_type_cargaison(self):
        return self.type_cargaison

    def ajouter_produit(self, produit):
        produit.calculer_frais(self.get_type_cargaison(), self.distance, self.express)
        self.produits.append(produit)

    def get_cout_total(self):
        t = self.get_type_cargaison()
        return sum(p.calculer_frais(t, self.distance, self.express) for p in self.produits)

    def __str__(self):
        e = "oui" if self.express else "non"
        return f"{self.get_type_cargaison()} - distance={self.distance} km - express={e} - produits={len(self.produits)} - cout={self.get_cout_total():,.2f} FCFA"
