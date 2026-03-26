from .produit import Produit


class Chimique(Produit):
    def __init__(self, libelle, poids, toxicite):
        super().__init__(libelle, poids)
        self.toxicite = toxicite

    def calculer_frais(self, type_cargaison, distance, express=False):
        cout = super().calculer_frais(type_cargaison, distance, express)
        return cout + self.toxicite * 10000 if type_cargaison == "Maritime" else cout

    def __str__(self):
        return f"{self.get_type()}({self.libelle}, {self.poids} kg, toxicite={self.toxicite})"
