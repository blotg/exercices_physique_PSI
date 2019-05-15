# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
from compilation.structure import Structure

def init_dossiers():
    if not os.path.exists("build"):
        os.makedirs("build")    
    if not os.path.exists("resultat"):
        os.makedirs("resultat")
    shutil.copy("sources/recueil.cls", "build/")
    shutil.copy("sources/prerequis.sty", "build/")
    shutil.copy("sources/exercice.sty", "build/")
    if not os.path.exists("build/lua"):
        os.makedirs("build/lua")
    for source_racine, dossiers, fichiers in os.walk("sources/lua/"):
        dest_racine = source_racine.replace("sources","build",1)
        for dossier in dossiers:
            if not os.path.exists(dest_racine + dossier):
                os.makedirs(dest_racine + dossier)
        for fichier in fichiers:
            shutil.copy(source_racine + fichier, dest_racine + fichier)
    with open("build/latexmkrc", "w") as fichier_latexmk:
        fichier_latexmk.write("""$pdflatex = 'lualatex --interaction=nonstopmode %O %S';""") 

def compilation_latex():
    processus = subprocess.Popen(["latexmk", "-pdf", "-output-directory=../resultat", "recueil.tex"], cwd="build", stdout=subprocess.PIPE)
    print(processus.communicate()[0].decode())

def compilation(classes, difficultes, contenu):
    print("Initialisation des dossiers ...")
    init_dossiers()
    print("Génération de la liste des exercices ...")
    exercices = Structure()
    exercices.selectionne(classes, difficultes)
    print(exercices)
    with open("build/recueil.tex", "w") as fichier_latex:
        fichier_latex.write(exercices.genere_latex(contenu))
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
