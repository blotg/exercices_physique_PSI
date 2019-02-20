# -*- coding: utf-8 -*-

import yaml

class Exercice:
    titre = ""
    theme = ""
    soustheme = ""
    difficulte = 0
    omis = True
    dossier = ""
    fichier = ""
    classes = []
    def __init__(self, dossier, fichier):
        self.dossier = dossier + "/"
        self.fichier = fichier
        entete = ""
        with open(self.dossier + self.fichier, "r") as fichier:
            for ligne in fichier:
                if ligne.startswith("%%"):
                    entete += ligne[2:]
        valeurs = yaml.load(entete)
        if "titre" in valeurs:
            self.titre = valeurs["titre"]
        if "theme" in valeurs:
            self.theme = valeurs["theme"]
        if "soustheme" in valeurs:
            self.soustheme = valeurs["soustheme"]
        if "difficulte" in valeurs:
            self.difficulte = valeurs["difficulte"]
        if "omis" in valeurs:
            self.omis = valeurs["omis"]
        if "classes" in valeurs:
            self.classes = valeurs["classes"]
    def inclusion(self):
        if not self.omis:
            return("\\inclure{../" + self.dossier + "}{" + self.fichier + "}\n")
        else:
            return("")
