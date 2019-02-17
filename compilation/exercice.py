# -*- coding: utf-8 -*-

class Exercice:
    theme = ""
    soustheme = ""
    difficulte = 0
    omis = True
    dossier = ""
    fichier = ""
    def __init__(self, dossier, fichier):
        self.dossier = dossier + "/"
        self.fichier = fichier
        entete = ""
        with open(self.dossier + self.fichier, "r") as fichier:
            for ligne in fichier:
                if ligne.startswith("%%"):
                    entete += ligne[2:]
        valeurs = yaml.load(entete)
        if "theme" in valeurs:
            self.theme = valeurs["theme"]
        if "soustheme" in valeurs:
            self.soustheme = valeurs["soustheme"]
        if "difficulte" in valeurs:
            self.difficulte = valeurs["difficulte"]
        if "omis" in valeurs:
            self.omis = valeurs["omis"]
