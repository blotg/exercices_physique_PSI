#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import os
except ImportError:
    print("La bibliothèque python \"os\" n'est pas installée et est nécessaire pour continuer ...")
    raise
try:
    import shutil
except ImportError:
    print("La bibliothèque python \"shutil\" n'est pas installée et est nécessaire pour continuer ...")
    raise
try:
    import subprocess
except ImportError:
    print("La bibliothèque python \"subprocess\" n'est pas installée et est nécessaire pour continuer ...")
    raise
try:
    import yaml
except ImportError:
    print("La bibliothèque python \"yaml\" n'est pas installée et est nécessaire pour continuer ...")
    raise
try:
    import gettext
    except ImportError:
    print("La bibliothèque python \"gettext\" n'est pas installée et est nécessaire pour continuer ...")
    raise
try:
    import argparse
except ImportError:
    print("La bibliothèque python \"argparse\" n'est pas installée et est nécessaire pour continuer ...")
    raise
def convertirArgparseMessages(s):
    dictionnaire = {'positional arguments':'Arguments positionnels',
                    'optional arguments':'Arguments optionnels',
                    'show this help message and exit':'Affiche ce message et quitte'}
    if s in dictionnaire:
        s = dictionnaire[s]
    return s
gettext.gettext = convertirArgparseMessages

#==============================================================================
# Initialisations relatives au traitement des paramètres
#==============================================================================
parseur = argparse.ArgumentParser(
        description="""Script de compilation du recueil d'exercices.
Chaque exercice doit être dans un fichier tex comportant un entête suivi de la commande \\exercice{Nom de l'exercice}.""")
parseur.add_argument(
    "-c", "--compiler",
    help = "Compile le recueil d'exercices.",
    action = "store_true")
parseur.add_argument(
    "-l", "--pdflatex",
    help = "Compilateur pdflatex à utiliser (lualatex par défaut) (non pris en compte à ce jour)",
    type=str,
    default="lualatex")
parseur.add_argument(
    "-n", "--nettoyer",
    help = "Supprime les fichiers qui ne sont plus utiles.",
    action = "store_true")
parseur.add_argument(
    "-N", "--nettoyer_tout",
    help = "Supprime tous les fichiers créés.",
    action = "store_true")
args = parseur.parse_args()

def init_dossiers():
    if not os.path.exists("build"):
        os.makedirs("build")    
    if not os.path.exists("resultat"):
        os.makedirs("resultat")
    shutil.copy("sources/recueil.cls", "build/")
    shutil.copy("sources/prerequis.sty", "build/")
    with open("build/latexmkrc", "w") as fichier_latexmk:
        fichier_latexmk.write("""$pdflatex = 'lualatex --interaction=batchmode %O %S';""") 

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

def parcours_dossiers():
    exercices = {}
    for racine, dossiers, fichiers in os.walk("sources/exercices"):
        for fichier in fichiers:
            if fichier.endswith(".tex"):
                e = Exercice(racine, fichier)
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

if args.compiler:
    print("Initialisation des dossiers ...")
    init_dossiers()
    print("Génération de la liste des exercices ...")
    genere_latex(parcours_dossiers())
    print("Compilation par latex ...")
    compilation_latex()
if args.nettoyer_tout:
    print("Suppression de tous les fichiers créés ...")
    if os.path.exists("build"):
        shutil.rmtree("build")
    if os.path.exists("resultat"):
        shutil.rmtree("resultat")
if args.nettoyer:
    print("Suppression des fichiers nécessaires à la compilation ...")
    if os.path.exists("build"):
        shutil.rmtree("build")
    for racine, dossiers, fichiers in os.walk("resultat"):
        for fichier in fichiers:
            if not fichier.endswith(".pdf"):
                os.remove(racine + "/" + fichier)
if not any([args.compiler, args.nettoyer_tout, args.nettoyer]):
    print("Aucune commande fournie. Utiliser -c pour compiler ou -h pour obtenir de l'aide")
