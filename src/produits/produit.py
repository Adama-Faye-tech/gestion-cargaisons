class Produit:
    def __init__(self, libelle, poids):
        self.libelle = libelle
        self.poids = poids

    def get_type(self):
        return self.__class__.__name__

    def calculer_frais(self, type_cargaison, distance, express=False):
        tarifs = {
            "Alimentaire": {"Routiere": 100, "Maritime": 90, "Aerienne": 300},
            "Chimique": {"Routiere": 0, "Maritime": 500, "Aerienne": 0},
            "Fragile": {"Routiere": 200, "Maritime": 0, "Aerienne": 400},
            "Incassable": {"Routiere": 80, "Maritime": 65, "Aerienne": 250},
            "Materiel": {"Routiere": 80, "Maritime": 65, "Aerienne": 250},
        }
        t = self.get_type()
        if t not in tarifs:
            t = "Materiel" if isinstance(self, Produit) else t
        n = tarifs[t][type_cargaison]
        if n <= 0:
            raise ValueError(f"Le produit {self.get_type()} ne peut pas etre transporte par {type_cargaison}.")
        return self.poids * distance * n * (1.1 if express else 1)

    def __str__(self):
        return f"{self.get_type()}({self.libelle}, {self.poids} kg)"
