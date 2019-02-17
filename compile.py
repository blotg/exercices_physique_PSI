#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess
import gettext
def convertirArgparseMessages(s):
    dictionnaire = {'positional arguments':'Arguments positionnels',
                    'optional arguments':'Arguments optionnels',
                    'show this help message and exit':'Affiche ce message et quitte'}
    if s in dictionnaire:
        s = dictionnaire[s]
    return s
gettext.gettext = convertirArgparseMessages
import argparse

parseur = argparse.ArgumentParser(
        description="Script de compilation du recueil d'exercices.")
parseur.add_argument(
    "-l", "--pdflatex",
    help = "Compilateur pdflatex à utiliser (lualatex par défaut)",
    type=str,
    default="lualatex")
args = parseur.parse_args()


if not os.path.exists("build"):
    os.makedirs("build")    
if not os.path.exists("resultat"):
    os.makedirs("resultat")

shutil.copy("sources/recueil.cls", "build/")
shutil.copy("sources/prerequis.sty", "build/")

with open("build/latexmkrc", "w") as fichier_latexmk:
    fichier_latexmk.write("""$pdflatex = 'lualatex --interaction=batchmode %O %S';""") 

source_latex = """\\documentclass{recueil}
\\begin{document}
"""
for racine, dossiers, fichiers in os.walk("sources/exercices"):
    for fichier in fichiers:
        source_latex += "\\input{../" + racine + "/" + fichier + "}\n"

source_latex += """\\end{document}"""
with open("build/recueil.tex", "w") as fichier_latex:
    fichier_latex.write(source_latex)

processus = subprocess.Popen(["latexmk", "-pdf", "-output-directory=../resultat", "recueil.tex"], cwd="build", stdout=subprocess.PIPE)
print(processus.communicate()[0].decode())
