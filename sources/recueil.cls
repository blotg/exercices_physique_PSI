\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{recueil}[2019/03/01 recueil]% Nom et version de la classe

\DeclareOption*{% Déclare les options qui sont reconnues
  \ClassWarning{recueil}{Unknown option '\CurrentOption'}% Aucune option n'est reconnue
}

\ProcessOptions\relax% Traite les options

\LoadClass[a4paper, 12pt]{article}% On utilise la classe article

\RequirePackage{prerequis}% Charge les prérequis du fichier "prerequis.sty"
\RequirePackage{exercice}% Charge les commandes exercice, question et subquestion

\geometry{left=1.5cm,right=1.5cm,top=2.5cm,bottom=2.5cm}% Défint la mise en page

\newcommand{\parttitle}{}
\titleformat{\part}
  {\Huge\scshape}
  {}
  {0pt}
  {\bariereFloat\newpage #1\renewcommand{\parttitle}{#1}}

\fancypagestyle{premiere}{% Mise en page de la page de garde
  \fancyhf{}%
  \fancyfoot[C]{\includegraphics[height=12px]{../sources/images/by-nc-sa.pdf}}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
}
\fancypagestyle{suivantes}{% Mise en page des autres pages
  \fancyhf{}%
  \fancyhead[L]{\parttitle}%scshape
  \fancyhead[R]{\nouppercase{\rightmark}}%
  \fancyfoot[C]{\thepage}%
  \fancyfoot[R]{\includegraphics[height=12px]{../sources/images/by-nc-sa.pdf}}%
  \renewcommand{\headrulewidth}{.4pt}%
  \renewcommand{\footrulewidth}{0pt}%
}

\pagestyle{suivantes}% Application de ces styles

\endinput
