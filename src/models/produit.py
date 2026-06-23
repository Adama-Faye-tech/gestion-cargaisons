class Produit:
    def __init__(self, libelle, poids):
        self.libelle = libelle
        self.poids = poids

    def get_type(self):
        return self.__class__.__name__

    def calculer_frais(self, type_cargaison, distance, express=False):
        type_produit = self.get_type()
        tarif = 0

        if type_produit == "Alimentaire":
            if type_cargaison == "Routiere":
                tarif = 100
            elif type_cargaison == "Maritime":
                tarif = 90
            elif type_cargaison == "Aerienne":
                tarif = 300
        elif type_produit == "Chimique":
            if type_cargaison == "Maritime":
                tarif = 500
        elif type_produit == "Fragile":
            if type_cargaison == "Routiere":
                tarif = 200
            elif type_cargaison == "Aerienne":
                tarif = 400
        elif type_produit == "Incassable" or type_produit == "Materiel":
            if type_cargaison == "Routiere":
                tarif = 80
            elif type_cargaison == "Maritime":
                tarif = 65
            elif type_cargaison == "Aerienne":
                tarif = 250

        if tarif == 0:
            raise ValueError(f"Le produit {type_produit} ne peut pas etre transporte par {type_cargaison}.")

        cout = self.poids * distance * tarif
        if express:
            cout = cout * 1.1
        return cout

    def __str__(self):
        return f"{self.get_type()}({self.libelle}, {self.poids} kg)"
