import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.cargaisons import CargaisonRoutiere, CargaisonMaritime, CargaisonAerienne
from src.gestion import GestionnaireCargaisons
from src.produits import Alimentaire, Chimique, Fragile, Incassable


def creer_cargaison():
    t = input("\n1.Routiere 2.Maritime 3.Aerienne\nChoix: ")
    d = float(input("Distance (km): "))
    e = input("Express? (o/n): ").lower() == "o"
    classes = {"1": CargaisonRoutiere, "2": CargaisonMaritime, "3": CargaisonAerienne}
    return classes[t](d, e) if t in classes else None


def creer_produit():
    t = input("\n1.Alimentaire 2.Chimique 3.Fragile 4.Incassable\nChoix: ")
    l = input("Libelle: ")
    p = float(input("Poids (kg): "))
    if t == "2":
        return Chimique(l, p, int(input("Toxicite: ")))
    classes = {"1": Alimentaire, "3": Fragile, "4": Incassable}
    return classes[t](l, p) if t in classes else None


def exemples(g):
    data = [
        (CargaisonRoutiere(150), [Alimentaire("Pommes", 10), Incassable("Fer", 50)]),
        (CargaisonMaritime(200), [Chimique("Acide", 25, 5), Incassable("Conteneur", 200)]),
        (CargaisonAerienne(500, True), [Fragile("Verre", 5), Alimentaire("Fruits", 20)]),
    ]
    for c, produits in data:
        for p in produits:
            c.ajouter_produit(p)
        g.ajouter_cargaison(c)


def main():
    g = GestionnaireCargaisons()
    while True:
        print("\n1.Afficher 2.Creer cargaison 3.Ajouter produit 4.Cout total 5.Exemples 6.Quitter")
        choix = input("Votre choix: ")
        if choix == "1":
            g.afficher_toutes_cargaisons()
        elif choix == "2":
            c = creer_cargaison()
            if c:
                g.ajouter_cargaison(c)
        elif choix == "3":
            if not g.cargaisons:
                print("Aucune cargaison")
            else:
                for i, c in enumerate(g.cargaisons, 1):
                    print(i, c.get_type_cargaison())
                i = int(input("Choisir cargaison: ")) - 1
                if 0 <= i < len(g.cargaisons):
                    try:
                        p = creer_produit()
                        if p:
                            g.cargaisons[i].ajouter_produit(p)
                            print("Produit ajoute")
                    except ValueError as e:
                        print("Erreur:", e)
        elif choix == "4":
            print(f"Cout total: {g.get_cout_total_toutes_cargaisons():,.2f} FCFA")
        elif choix == "5":
            try:
                exemples(g)
                print("Exemples crees")
            except ValueError as e:
                print("Erreur:", e)
        elif choix == "6":
            break


main()
