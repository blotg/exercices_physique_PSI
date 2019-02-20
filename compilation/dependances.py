# -*- coding: utf-8 -*-

def verifier_dependances():
    satisfaites = True
    try:
        import os
    except ImportError:
        print("La bibliothèque python \"os\" n'est pas installée et est nécessaire pour continuer.")
        satisfaites = False
    try:
        import shutil
    except ImportError:
        print("La bibliothèque python \"shutil\" n'est pas installée et est nécessaire pour continuer.")
        satisfaites = False
    try:
        import subprocess
    except ImportError:
        print("La bibliothèque python \"subprocess\" n'est pas installée et est nécessaire pour continuer.")
        satisfaites = False
    try:
        import yaml
    except ImportError:
        print("La bibliothèque python \"yaml\" n'est pas installée et est nécessaire pour continuer.")
        satisfaites = False
    try:
        import gettext
    except ImportError:
        print("La bibliothèque python \"gettext\" n'est pas installée et est nécessaire pour continuer.")
        satisfaites = False
    try:
        import argparse
    except ImportError:
        print("La bibliothèque python \"argparse\" n'est pas installée et est nécessaire pour continuer.")
        satisfaites = False
    try:
        import re
    except ImportError:
        print("La bibliothèque python \"re\" n'est pas installée et est nécessaire pour continuer.")
        satisfaites = False
    
    programmes_systeme = ["latexmk", "lualatex"]
    for prog in programmes_systeme:
        if shutil.which(prog) == None:
            print(prog + " n'est pas installé et est indiscipensable à la compilation.")
            satisfaites = False
    return satisfaites
