import os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.cargaisons import CargaisonRoutiere, CargaisonMaritime, CargaisonAerienne
from src.gestion import GestionnaireCargaisons
from src.produits import Alimentaire, Chimique, Fragile, Incassable


def creer_cargaison():
    type_cargaison = input("\n1.Routiere 2.Maritime 3.Aerienne\nChoix: ")
    distance = float(input("Distance (km): "))
    est_express = input("Express? (o/n): ").lower() == "o"
    if type_cargaison == "1":
        return CargaisonRoutiere(distance, est_express)
    elif type_cargaison == "2":
        return CargaisonMaritime(distance, est_express)
    elif type_cargaison == "3":
        return CargaisonAerienne(distance, est_express)
    return None


def creer_produit():
    type_produit = input("\n1.Alimentaire 2.Chimique 3.Fragile 4.Incassable\nChoix: ")
    libelle = input("Libelle: ")
    poids = float(input("Poids (kg): "))
    if type_produit == "2":
        toxicite = int(input("Toxicite: "))
        return Chimique(libelle, poids, toxicite)
    elif type_produit == "1":
        return Alimentaire(libelle, poids)
    elif type_produit == "3":
        return Fragile(libelle, poids)
    elif type_produit == "4":
        return Incassable(libelle, poids)
    return None


def exemples(gestionnaire):
    cargaison_routiere = CargaisonRoutiere(150)
    cargaison_routiere.ajouter_produit(Alimentaire("Pommes", 10))
    cargaison_routiere.ajouter_produit(Incassable("Fer", 50))
    gestionnaire.ajouter_cargaison(cargaison_routiere)

    cargaison_maritime = CargaisonMaritime(200)
    cargaison_maritime.ajouter_produit(Chimique("Acide", 25, 5))
    cargaison_maritime.ajouter_produit(Incassable("Conteneur", 200))
    gestionnaire.ajouter_cargaison(cargaison_maritime)

    cargaison_aerienne = CargaisonAerienne(500, True)
    cargaison_aerienne.ajouter_produit(Fragile("Verre", 5))
    cargaison_aerienne.ajouter_produit(Alimentaire("Fruits", 20))
    gestionnaire.ajouter_cargaison(cargaison_aerienne)


def main():
    gestionnaire = GestionnaireCargaisons()
    while True:
        print("\n1.Afficher 2.Creer cargaison 3.Ajouter produit 4.Cout total 5.Exemples 6.Quitter")
        choix = input("Votre choix: ")
        if choix == "1":
            gestionnaire.afficher_toutes_cargaisons()
        elif choix == "2":
            cargaison = creer_cargaison()
            if cargaison:
                gestionnaire.ajouter_cargaison(cargaison)
        elif choix == "3":
            if not gestionnaire.cargaisons:
                print("Aucune cargaison")
            else:
                for index_cargaison in range(len(gestionnaire.cargaisons)):
                    print(index_cargaison + 1, gestionnaire.cargaisons[index_cargaison].get_type_cargaison())
                index_cargaison = int(input("Choisir cargaison: ")) - 1
                if 0 <= index_cargaison < len(gestionnaire.cargaisons):
                    try:
                        produit = creer_produit()
                        if produit:
                            gestionnaire.cargaisons[index_cargaison].ajouter_produit(produit)
                            print("Produit ajoute")
                    except ValueError as erreur:
                        print("Erreur:", erreur)
        elif choix == "4":
            print(f"Cout total: {gestionnaire.get_cout_total_toutes_cargaisons():,.2f} FCFA")
        elif choix == "5":
            try:
                exemples(gestionnaire)
                print("Exemples crees")
            except ValueError as erreur:
                print("Erreur:", erreur)
        elif choix == "6":
            break


main()
