class GestionnaireCargaisons:
    def __init__(self):
        self.cargaisons = []

    def ajouter_cargaison(self, cargaison):
        self.cargaisons.append(cargaison)

    def afficher_toutes_cargaisons(self):
        if not self.cargaisons:
            print("Aucune cargaison enregistree.")
            return
        for index_cargaison in range(len(self.cargaisons)):
            cargaison = self.cargaisons[index_cargaison]
            print(f"{index_cargaison + 1}. {cargaison}")
            for index_produit in range(len(cargaison.produits)):
                print(f"   - {cargaison.produits[index_produit]}")

    def get_cout_total_toutes_cargaisons(self):
        cout_total = 0
        for cargaison in self.cargaisons:
            cout_total = cout_total + cargaison.get_cout_total()
        return cout_total
