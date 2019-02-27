#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#==============================================================================
# Import des différentes bibliothèques nécessaires et vérification des dépendances
#==============================================================================

from compilation import dependances
from compilation import dossiers
from compilation import parseur

if dependances.verifier_dependances():
    pars = parseur.Parseur()
    if pars.args.compiler:
        dossiers.compilation(pars.args.classes, pars.args.difficulte, pars.args.contenu)
    if pars.args.nettoyer_tout:
        dossiers.nettoyage()
    if pars.args.nettoyer:
        dossiers.nettoyage_integral()
    if not any([pars.args.compiler, pars.args.nettoyer_tout, pars.args.nettoyer]):
        print("Aucune commande fournie. Utiliser -c pour compiler ou -h pour obtenir de l'aide")
else:
    print("Abandon")