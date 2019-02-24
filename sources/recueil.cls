\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{recueil}[2019/02/07 recueil]

% Aucune option n'est reconnue
\DeclareOption*{
  \ClassWarning{recueil}{Unknown option '\CurrentOption'}
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


\begin{luacode*}
  reponses = "";
  function ajouteReponse(nQuestion, reponse)
    reponses = reponses .. "\\par\\noindent\\rlap{" .. nQuestion .. ".}\\tabto{1.4em}" .. reponse;
  end
\end{luacode*}

\newcounter{subquestion}
\newcommand{\subquestion}{%
  \stepcounter{subquestion}%
  \tabto{1.4em}\alph{subquestion})\tabto{2.7em}
}
\newcounter{question}% Définition de la commande \question
\newcommand{\question}{%
  \par\stepcounter{question}%
  \setcounter{subquestion}{0}%
  \noindent\rlap{\thequestion.}\tabto{1.4em}
}
\newcounter{exercice}
\newcommand{\exercice}[1]{%
  \stepcounter{exercice}%
  \setcounter{question}{0}%
  \subsubsection*{Exercice \theexercice{} - #1}
}

\newcommand{\reponse}[1]{
  \luadirect{
    ajouteReponse( \luastring{\thequestion}, \luastringN{#1} );
  }
}
\newcommand{\afficheReponse}{
  \luadirect{tex.print(reponses)}
}

\endinput
