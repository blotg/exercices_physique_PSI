# -*- coding: utf-8 -*-

import os
from compilation import exercice
import re

class Structure:
    s = []
    classes = ["MPSI", "PCSI", "PTSI", "MP", "PC", "PSI"]
    difficultes = [0,1,2,3,4]
    def __init__(self):
        self.peuple()
    
    def peuple(self):
        themes = os.listdir("sources/exercices")
        themes.sort()
        for theme in themes:
            chemin = "sources/exercices/" + theme
            if os.path.isfile(chemin):
                racine,fichier = os.path.split(chemin)
                if fichier.endswith(".tex"):
                    e = exercice.Exercice(racine, fichier)
                    self.s.append(e)
            elif os.path.isdir(chemin):
                exos = os.listdir("sources/exercices/" + theme)
                exos.sort()
                L = []
                for exo in exos:
                    chemin = "sources/exercices/" + theme + "/" + exo
                    if os.path.isfile(chemin):
                        racine,fichier = os.path.split(chemin)
                        if fichier.endswith(".tex"):
                            e = exercice.Exercice(racine, fichier)
                            L.append(e)
                if len(L) != 0:
                    self.s.append((theme[3:].replace("_"," "), L))
                    
    def __str__(self):
        chaine = ""
        for element in self.s:
            if type(element) != tuple:
                chaine += "|-- " + element + "\n"
            else:
                (theme, L) = element
                chaine += "|-- " + theme + "\n"
                for exo in L:
                    chaine += "|   |-- " + str(exo) + "\n"
        chaine = chaine[:-1]
        return chaine
    
    def selectionne(self, classes, difficultes):
        if classes:
            self.classes = classes
        if difficultes:
            self.difficultes = difficultes
        temp_s = []
        for element in self.s:
            if type(element) != tuple:
                if any(x in element.classes for x in self.classes) and element.difficulte in self.difficultes:
                    temp_s.append(element)
            else:
                (theme, L) = element
                temp_L = []
                for exo in L:
                    if any(x in exo.classes for x in self.classes) and exo.difficulte in self.difficultes and not exo.omis:
                        temp_L.append(exo)
                if len(temp_L) != 0:
                    temp_s.append((theme, temp_L))
        self.s = temp_s
    
    def genere_latex(self, contenu):
        if not contenu:
            contenu = []
        source_latex = ""
        with open("sources/template.tex", "r") as fichier:
            for ligne in fichier:
                source_latex += ligne
        motif = "\\\\newcommand\{\\\\classes\}\{\}"
        remplacement = "\\\\newcommand{\\classes}{" + str(self.classes).replace("'","")[1:-1] + "}"
        source_latex = re.sub(motif, remplacement, source_latex)
        if True:
            enonces = ""
            for element in self.s:
                if type(element) != tuple:
                    enonces += element.inclusion()
                else:
                    (theme, L) = element
                    enonces += "\\section{" + theme + "}\n"
                    for exo in L:
                        enonces += exo.inclusion()
            source_latex = re.sub("\\\\afficheEnonces", enonces, source_latex)
        if not "R" in contenu:
            motif = "(\\\\begin\{reponses\}).*?(\\\\end\{reponses\})"
            source_latex = re.sub(motif, "", source_latex, flags=re.DOTALL)
        return source_latex
