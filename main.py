#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Application de gestion des cargaisons
Architecture: Model-View-Controller (MVC)
"""

import os
import sys

# Ajouter le répertoire courant au path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.controllers import CargaisonController


def main():
    """Point d'entrée de l'application"""
    controller = CargaisonController()
    controller.executer()


if __name__ == "__main__":
    main()
