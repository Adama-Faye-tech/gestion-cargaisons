class InputView:
    @staticmethod
    def demander_choix(message="Votre choix"):
        return input(f"\n{message}: ")

    @staticmethod
    def demander_distance():
        return float(input("Distance (km): "))

    @staticmethod
    def demander_express():
        return input("Express? (o/n): ").lower() == "o"

    @staticmethod
    def demander_libelle():
        return input("Libelle du produit: ")

    @staticmethod
    def demander_poids():
        return float(input("Poids (kg): "))

    @staticmethod
    def demander_toxicite():
        return int(input("Niveau de toxicite: "))

    @staticmethod
    def demander_index_cargaison(nb_cargaisons):
        for i in range(nb_cargaisons):
            print(f"{i + 1}. Cargaison {i + 1}")
        return int(input("Choisir une cargaison: ")) - 1
