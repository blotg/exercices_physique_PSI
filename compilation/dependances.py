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

programmes_systeme = ["latexmk", "lualatex"]
for prog in programmes_systeme:
    if shutil.which(prog) == None:
        print(prog + " n'est pas installé et est indiscipensable à la compilation.")
        raise OSError()

