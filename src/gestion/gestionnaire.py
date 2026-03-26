class GestionnaireCargaisons:
    def __init__(self):
        self.cargaisons = []

    def ajouter_cargaison(self, cargaison):
        self.cargaisons.append(cargaison)

    def afficher_toutes_cargaisons(self):
        if not self.cargaisons:
            print("Aucune cargaison enregistree.")
            return
        for i, c in enumerate(self.cargaisons, 1):
            print(f"{i}. {c}")
            for p in c.produits:
                print(f"   - {p}")

    def get_cout_total_toutes_cargaisons(self):
        return sum(c.get_cout_total() for c in self.cargaisons)
