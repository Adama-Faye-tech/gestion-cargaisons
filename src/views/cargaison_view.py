class CargaisonView:
    @staticmethod
    def afficher_menu_principal():
        print("\n" + "="*50)
        print("GESTION DES CARGAISONS")
        print("="*50)
        print("1. Afficher toutes les cargaisons")
        print("2. Creer une nouvelle cargaison")
        print("3. Ajouter un produit a une cargaison")
        print("4. Afficher le cout total")
        print("5. Charger des exemples")
        print("6. Quitter")
        print("="*50)

    @staticmethod
    def afficher_menu_type_cargaison():
        print("\nType de cargaison:")
        print("1. Routiere")
        print("2. Maritime")
        print("3. Aerienne")

    @staticmethod
    def afficher_menu_type_produit():
        print("\nType de produit:")
        print("1. Alimentaire")
        print("2. Chimique")
        print("3. Fragile")
        print("4. Incassable")

    @staticmethod
    def afficher_cargaisons(cargaisons):
        if not cargaisons:
            print("\nAucune cargaison enregistree.")
            return
        print("\n" + "-"*50)
        print("LISTE DES CARGAISONS")
        print("-"*50)
        for index, cargaison in enumerate(cargaisons):
            print(f"{index + 1}. {cargaison}")
            for index_produit, produit in enumerate(cargaison.produits):
                print(f"   {index_produit + 1}. {produit}")
        print("-"*50)

    @staticmethod
    def afficher_cout_total(cout):
        print(f"\nCout total de toutes les cargaisons: {cout:,.2f} FCFA")

    @staticmethod
    def afficher_message(message):
        print(f"\n>>> {message}")

    @staticmethod
    def afficher_erreur(message):
        print(f"\n[ERREUR] {message}")

    @staticmethod
    def afficher_succes(message):
        print(f"\n[OK] {message}")
