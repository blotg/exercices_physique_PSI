# -*- coding: utf-8 -*-

import gettext
def traduirArgparseMessages(s):
    dictionnaire = {'positional arguments':'Arguments positionnels',
                    'optional arguments':'Arguments optionnels',
                    'show this help message and exit':'Affiche ce message et quitte'}
    if s in dictionnaire:
        s = dictionnaire[s]
    return s
gettext.gettext = traduirArgparseMessages
import argparse

import re

class TraiteIntervalle(argparse.Action):
    def __call__(self, parseur, namespace, valeurs, option_string=None):
        l = []
        for valeur in valeurs:
            if re.fullmatch("([0-9]+)-([0-9]+)", valeur):
                [debut,fin] = valeur.split("-")
                l.extend(list(range(int(debut), int(fin)+1)))
            elif re.fullmatch("[0-9]+", valeur):
                l.append(int(valeur))
            else:
                parseur.error("'" + valeur + "' n'est pas un intervalle. Formes attendues : '0-3' ou '2'.")
                l.append(int(valeur))
            setattr(namespace, self.dest, l)

class Parseur:
    def __init__(self):
        self.parseur = argparse.ArgumentParser(
        description="""Script de compilation du recueil d'exercices.
Chaque exercice doit être dans un fichier tex comportant un entête suivi de la commande \\exercice{Nom de l'exercice}.""")
        self.parseur.add_argument(
            "-c", "--compiler",
            help = "Compile le recueil d'exercices.",
            action = "store_true")
        self.parseur.add_argument(
            "-p", "--pdflatex",
            help = "Compilateur pdflatex à utiliser (lualatex par défaut) (non pris en compte à ce jour)",
            type=str,
            default="lualatex")
        self.parseur.add_argument(
            "-n", "--nettoyer",
            help = "Supprime les fichiers qui ne sont plus utiles.",
            action = "store_true")
        self.parseur.add_argument(
            "-N", "--nettoyer_tout",
            help = "Supprime tous les fichiers créés.",
            action = "store_true")
        self.parseur.add_argument(
            "-l", "--classes",
            nargs='+',
            help = "Précises les classes pour lesquelles compiler le recueil.")
        self.parseur.add_argument(
            "-d", "--difficulte",
            nargs='+',
            action=TraiteIntervalle,
            help = "Précises les difficultés des exercices du recueil.")
        self.args = self.parseur.parse_args()