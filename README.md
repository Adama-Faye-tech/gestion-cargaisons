# Gestion des Cargaisons

**EXAMEN PYTHON AVEC ALLY TALL NIANG**

## Description

Application de gestion de cargaisons pour l'entreprise de transport "GP du Monde". 
L'application permet de gérer différents types de cargaisons (maritime, aérienne, routière) 
et de produits (alimentaire, chimique, matériel) avec des règles de transport spécifiques.

## Architecture

Le projet utilise le pattern **Model-View-Controller (MVC)** pour une meilleure organisation du code :

### Structure des répertoires

```
src/
├── models/                          # Couche Modèle
│   ├── produit.py                  # Classe de base pour les produits
│   ├── alimentaire.py
│   ├── chimique.py
│   ├── fragile.py
│   ├── incassable.py
│   ├── materiel.py
│   ├── cargaison.py                # Classe de base pour les cargaisons
│   ├── cargaison_routiere.py
│   ├── cargaison_maritime.py
│   ├── cargaison_aerienne.py
│   └── gestionnaire_cargaisons.py  # Gestion globale des cargaisons
├── views/                           # Couche Présentation
│   ├── cargaison_view.py           # Affichage des cargaisons
│   └── input_view.py               # Gestion des entrées utilisateur
├── controllers/                     # Couche Contrôleur
│   └── cargaison_controller.py     # Logique métier et coordination
└── __init__.py
main.py                              # Point d'entrée de l'application
```

### Pattern MVC

- **Models (src/models/)** : Classes métier (Produit, Cargaison, GestionnaireCargaisons)
- **Views (src/views/)** : Interface utilisateur et affichage
- **Controllers (src/controllers/)** : Logique de coordination et métier

## Fonctionnalités

- ✅ Création de cargaisons (maritime, aérienne, routière)
- ✅ Ajout de produits (alimentaire, chimique, fragile, incassable)
- ✅ Calcul automatique des frais de transport selon les tarifs définis
- ✅ Gestion des contraintes de transport (chimique uniquement maritime, fragile jamais maritime)
- ✅ Option express (coût × 1.1)
- ✅ Validation du nombre de produits (1 à 1000 par cargaison)
- ✅ Affichage détaillé de toutes les cargaisons et produits
- ✅ Calcul du coût total

## Prérequis

- Python 3.7 ou supérieur
- Aucune bibliothèque externe requise

## Installation

### Méthode 1 : Git Clone

```bash
git clone https://github.com/Adama-Faye-tech/gestion-cargaisons.git
cd gestion-cargaisons
python main.py
```

### Méthode 2 : À partir d'un fichier ZIP

1. Décompressez le fichier `gestion_cargaisons.zip`
2. Ouvrez un terminal dans le dossier décompressé
3. Exécutez : `python main.py`

## Utilisation

Lancez l'application avec :

```bash
python main.py
```

Vous verrez un menu principal avec les options suivantes :

1. **Afficher toutes les cargaisons** - Liste toutes les cargaisons et leurs produits
2. **Créer une nouvelle cargaison** - Crée une nouvelle cargaison (choisir le type, distance, express)
3. **Ajouter un produit à une cargaison** - Ajoute un produit à une cargaison existante
4. **Afficher le coût total** - Affiche le coût total de toutes les cargaisons
5. **Charger des exemples** - Crée des cargaisons d'exemple
6. **Quitter** - Ferme l'application

## Exemple d'utilisation

```python
from src.models import CargaisonRoutiere, Alimentaire, Incassable, GestionnaireCargaisons

# Créer une cargaison
cargaison = CargaisonRoutiere(distance=150, express=False)

# Ajouter des produits
cargaison.ajouter_produit(Alimentaire("Pommes", 10))
cargaison.ajouter_produit(Incassable("Fer", 50))

# Ajouter la cargaison au gestionnaire
gestionnaire = GestionnaireCargaisons()
gestionnaire.ajouter_cargaison(cargaison)

# Afficher le coût total
cout_total = gestionnaire.get_cout_total_toutes_cargaisons()
print(f"Coût total : {cout_total:,.2f} FCFA")
```

## Tarifs des produits

Les tarifs varient selon le type de cargaison et le type de produit :

| Produit    | Routière | Maritime | Aérienne |
|------------|----------|----------|----------|
| Alimentaire| 100      | 90       | 300      |
| Chimique   | ❌        | 500      | ❌        |
| Fragile    | 200      | ❌        | 400      |
| Incassable | 80       | 65       | 250      |
| Matériel   | 80       | 65       | 250      |

**Formule de calcul :**
- Coût = Poids (kg) × Distance (km) × Tarif (FCFA/kg/km)
- Si express : Coût × 1.1
- Si chimique en maritime : Coût + (Toxicité × 10,000)

## Architecture en images

```
┌─────────────────────────────────────────────────┐
│              APPLICATION (main.py)               │
└────────────────────┬────────────────────────────┘
                     │
         ┌───────────┴───────────┐
         │                       │
    ┌────▼──────┐          ┌─────▼─────┐
    │ CONTROLLER│◄────────►│   VIEWS   │
    │(Logique)  │          │(Affichage)│
    └────┬──────┘          └───────────┘
         │
    ┌────▼──────────────────────┐
    │     MODELS (Métier)       │
    │ ├─ Produits              │
    │ ├─ Cargaisons            │
    │ └─ Gestionnaire           │
    └───────────────────────────┘
```

## Auteur

Adama Faye

## Licence

MIT

---

**Dernière mise à jour** : Version MVC - 2024
