#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import shutil
import subprocess

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

print(source_latex)

processus = subprocess.Popen(["latexmk", "-pdf", "-cd", "-output-directory=../resultat", "recueil.tex"], cwd="build", stdout=subprocess.PIPE)
print(processus.communicate())
