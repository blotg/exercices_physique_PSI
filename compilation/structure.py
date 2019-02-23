# -*- coding: utf-8 -*-

import os
from compilation import exercice

class Structure:
    s = {}
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
        if classes == None:
            classes = ["PC", "MP", "PSI"]
        if difficultes == None:
            difficultes = list(range(0,100))
        temp_s = {}
        for theme in self.s:
            theme_vide = True
            for soustheme in self.s[theme]:
                soustheme_vide = True
                for e in self.s[theme][soustheme]:
                    if any(x in e.classes for x in classes) and e.difficulte in difficultes:
                        if soustheme_vide:
                            if theme_vide:
                                temp_s[theme] = {}
                            temp_s[theme][soustheme] = []
                        temp_s[theme][soustheme].append(e)
        self.s = temp_s
        
    def genere_latex(self):
        source_latex = "\\documentclass{recueil}\n\\begin{document}"
        for theme in self.s:
            source_latex += "\\section{" + theme + "}\n"
            for soustheme in self.s[theme]:
                source_latex += "\\subsection{" + soustheme + "}\n"
                for e in self.s[theme][soustheme]:
                    source_latex += e.inclusion()
        source_latex += """\\end{document}"""
        return source_latex