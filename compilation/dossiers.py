# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
from compilation import exercice

def init_dossiers():
    if not os.path.exists("build"):
        os.makedirs("build")    
    if not os.path.exists("resultat"):
        os.makedirs("resultat")
    shutil.copy("sources/recueil.cls", "build/")
    shutil.copy("sources/prerequis.sty", "build/")
    with open("build/latexmkrc", "w") as fichier_latexmk:
        fichier_latexmk.write("""$pdflatex = 'lualatex --interaction=batchmode %O %S';""") 

def parcours_dossiers():
    exercices = {}
    for racine, dossiers, fichiers in os.walk("sources/exercices"):
        for fichier in fichiers:
            if fichier.endswith(".tex"):
                e = exercice.Exercice(racine, fichier)
                if not e.theme in exercices:
                    exercices[e.theme] = {}
                if not e.soustheme in exercices[e.theme]:
                    exercices[e.theme][e.soustheme] = []
                exercices[e.theme][e.soustheme].append(e)
    return exercices

def genere_latex(exercices):
    source_latex = """\\documentclass{recueil}
    \\begin{document}
    """
    for theme in exercices:
        source_latex += "\\section{" + theme + "}\n"
        for soustheme in exercices[theme]:
            source_latex += "\\subsection{" + soustheme + "}\n"
            for e in exercices[theme][soustheme]:
                source_latex += "\\inclure{../" + e.dossier + "}{" + e.fichier + "}\n"
    source_latex += """\\end{document}"""
    with open("build/recueil.tex", "w") as fichier_latex:
        fichier_latex.write(source_latex)
        
def compilation_latex():
    processus = subprocess.Popen(["latexmk", "-pdf", "-output-directory=../resultat", "recueil.tex"], cwd="build", stdout=subprocess.PIPE)
    print(processus.communicate()[0].decode())

def compilation():
    print("Initialisation des dossiers ...")
    init_dossiers()
    print("Génération de la liste des exercices ...")
    genere_latex(parcours_dossiers())
    print("Compilation par latex ...")
    compilation_latex()

def nettoyage():
    print("Suppression de tous les fichiers créés ...")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("resultat"):
        shutil.rmtree("resultat")

def nettoyage_integral():
    print("Suppression des fichiers nécessaires à la compilation ...")
    if os.path.exists("build"):
        shutil.rmtree("build")
    for racine, _, fichiers in os.walk("resultat"):
        for fichier in fichiers:
            if not fichier.endswith(".pdf"):
                os.remove(racine + "/" + fichier)