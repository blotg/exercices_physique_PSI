\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{dossier}[2019/02/07 dossier]

% Aucune option n'est reconnue
\DeclareOption*{
  \ClassWarning{dossier}{Unknown option '\CurrentOption'}
}

\PassOptionsToClass{12pt}{article}% On utilise la classe article avec 12pt

\ProcessOptions\relax% Traite les options

\LoadClass[a4paper]{article}

\RequirePackage{prerequis}% Charge les prérequis du fichier "prerequis.sty"

\geometry{left=1cm,right=1cm,top=1.5cm,bottom=2cm}% Défint la mise en page.

\fancypagestyle{premiere}{% Mise en page de la page de garde
  \fancyhf{}
  \fancyfoot[C]{\thepage}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{suivantes}{% Mise en page des autres pages
  \fancyhf{}
  \fancyfoot[C]{\thepage}
  \renewcommand{\headrulewidth}{0pt}
  \renewcommand{\footrulewidth}{0pt}
}

\pagestyle{suivantes}% Application de ces styles
\AtBeginDocument{\thispagestyle{premiere}}

\endinput
