from src.models import (
    CargaisonRoutiere, CargaisonMaritime, CargaisonAerienne,
    Alimentaire, Chimique, Fragile, Incassable,
    GestionnaireCargaisons
)
from src.views import CargaisonView, InputView


class CargaisonController:
    def __init__(self):
        self.gestionnaire = GestionnaireCargaisons()
        self.view = CargaisonView()
        self.input_view = InputView()

    def creer_cargaison(self):
        """Crée une nouvelle cargaison"""
        try:
            self.view.afficher_menu_type_cargaison()
            type_cargaison = self.input_view.demander_choix("Type de cargaison")
            distance = self.input_view.demander_distance()
            express = self.input_view.demander_express()

            if type_cargaison == "1":
                cargaison = CargaisonRoutiere(distance, express)
            elif type_cargaison == "2":
                cargaison = CargaisonMaritime(distance, express)
            elif type_cargaison == "3":
                cargaison = CargaisonAerienne(distance, express)
            else:
                self.view.afficher_erreur("Choix invalide!")
                return None

            self.gestionnaire.ajouter_cargaison(cargaison)
            self.view.afficher_succes("Cargaison cree avec succes!")
            return cargaison
        except ValueError as e:
            self.view.afficher_erreur(str(e))
            return None

    def creer_produit(self):
        """Crée un nouveau produit"""
        try:
            self.view.afficher_menu_type_produit()
            type_produit = self.input_view.demander_choix("Type de produit")
            libelle = self.input_view.demander_libelle()
            poids = self.input_view.demander_poids()

            if type_produit == "1":
                produit = Alimentaire(libelle, poids)
            elif type_produit == "2":
                toxicite = self.input_view.demander_toxicite()
                produit = Chimique(libelle, poids, toxicite)
            elif type_produit == "3":
                produit = Fragile(libelle, poids)
            elif type_produit == "4":
                produit = Incassable(libelle, poids)
            else:
                self.view.afficher_erreur("Choix invalide!")
                return None

            return produit
        except ValueError as e:
            self.view.afficher_erreur(str(e))
            return None

    def ajouter_produit_a_cargaison(self):
        """Ajoute un produit à une cargaison"""
        try:
            if not self.gestionnaire.cargaisons:
                self.view.afficher_message("Aucune cargaison disponible!")
                return

            index_cargaison = self.input_view.demander_index_cargaison(len(self.gestionnaire.cargaisons))

            if not (0 <= index_cargaison < len(self.gestionnaire.cargaisons)):
                self.view.afficher_erreur("Index invalide!")
                return

            produit = self.creer_produit()
            if produit:
                self.gestionnaire.cargaisons[index_cargaison].ajouter_produit(produit)
                self.view.afficher_succes("Produit ajoute a la cargaison!")
        except ValueError as e:
            self.view.afficher_erreur(str(e))

    def afficher_toutes_cargaisons(self):
        """Affiche toutes les cargaisons"""
        self.view.afficher_cargaisons(self.gestionnaire.cargaisons)

    def afficher_cout_total(self):
        """Affiche le coût total"""
        cout = self.gestionnaire.get_cout_total_toutes_cargaisons()
        self.view.afficher_cout_total(cout)

    def charger_exemples(self):
        """Charge des cargaisons d'exemple"""
        try:
            # Cargaison routiere
            cargaison_routiere = CargaisonRoutiere(150)
            cargaison_routiere.ajouter_produit(Alimentaire("Pommes", 10))
            cargaison_routiere.ajouter_produit(Incassable("Fer", 50))
            self.gestionnaire.ajouter_cargaison(cargaison_routiere)

            # Cargaison maritime
            cargaison_maritime = CargaisonMaritime(200)
            cargaison_maritime.ajouter_produit(Chimique("Acide", 25, 5))
            cargaison_maritime.ajouter_produit(Incassable("Conteneur", 200))
            self.gestionnaire.ajouter_cargaison(cargaison_maritime)

            # Cargaison aerienne
            cargaison_aerienne = CargaisonAerienne(500, True)
            cargaison_aerienne.ajouter_produit(Fragile("Verre", 5))
            cargaison_aerienne.ajouter_produit(Alimentaire("Fruits", 20))
            self.gestionnaire.ajouter_cargaison(cargaison_aerienne)

            self.view.afficher_succes("Exemples charges avec succes!")
        except ValueError as e:
            self.view.afficher_erreur(str(e))

    def executer(self):
        """Boucle principale de l'application"""
        while True:
            self.view.afficher_menu_principal()
            choix = self.input_view.demander_choix("Votre choix")

            if choix == "1":
                self.afficher_toutes_cargaisons()
            elif choix == "2":
                self.creer_cargaison()
            elif choix == "3":
                self.ajouter_produit_a_cargaison()
            elif choix == "4":
                self.afficher_cout_total()
            elif choix == "5":
                self.charger_exemples()
            elif choix == "6":
                self.view.afficher_message("Au revoir!")
                break
            else:
                self.view.afficher_erreur("Choix invalide!")
