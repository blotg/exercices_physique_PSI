# -*- coding: utf-8 -*-

import os
from compilation import exercice
import re

class Structure:
    s = {}
    classes = ["MPSI", "PCSI", "PTSI", "MP", "PC", "PSI"]
    difficultes = [0,1,2,3,4]
    def __init__(self,dossier):
        for racine, dossiers, fichiers in os.walk(dossier):
            for fichier in fichiers:
                if fichier.endswith(".tex"):
                    e = exercice.Exercice(racine, fichier)
                    if not e.theme in self.s:
                        self.s[e.theme] = {}
                    if not e.soustheme in self.s[e.theme]:
                        self.s[e.theme][e.soustheme] = []
                    self.s[e.theme][e.soustheme].append(e)
    
    def __str__(self):
        chaine = ""
        for theme in self.s:
            chaine += theme + "\n"
            for soustheme in self.s[theme]:
                chaine += "|--|" + soustheme + "\n"
                for e in self.s[theme][soustheme]:
                    chaine += "|  |-- "
                    if e.omis:
                        chaine += "("
                    chaine += e.titre
                    for i in range(e.difficulte):
                        chaine += "*"
                    if e.omis:
                        chaine += ")"
                    chaine += "\n"
        chaine = chaine[:-1]
        return chaine
    
    def selectionne(self, classes, difficultes):
        if classes:
            self.classes = classes
        if difficultes:
            self.difficultes = difficultes
        temp_s = {}
        for theme in self.s:
            theme_vide = True
            for soustheme in self.s[theme]:
                soustheme_vide = True
                for e in self.s[theme][soustheme]:
                    if any(x in e.classes for x in self.classes) and e.difficulte in self.difficultes:
                        if soustheme_vide:
                            if theme_vide:
                                temp_s[theme] = {}
                                theme_vide = False
                            temp_s[theme][soustheme] = []
                            soustheme_vide = False
                        temp_s[theme][soustheme].append(e)
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
            for theme in self.s:
                enonces += "\\section{" + theme + "}\n"
                for soustheme in self.s[theme]:
                    enonces += "\\subsection{" + soustheme + "}\n"
                    for e in self.s[theme][soustheme]:
                        enonces += e.inclusion()
            source_latex = re.sub("\\\\afficheEnonces", enonces, source_latex)
        if not "R" in contenu:
            motif = "(\\\\begin\{reponses\}).*?(\\\\end\{reponses\})"
            source_latex = re.sub(motif, "", source_latex, flags=re.DOTALL)
        return source_latex
