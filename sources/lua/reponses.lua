Reponses = {chaine = "", tempExercice = "", tempSubsection = "", tempSection = ""}-- Initialisation de l'objet Reponses

function Reponses:section(nSection, titre)-- Ajoute une section
    Reponses.tempSection = "\\setcounter{section}{" .. nSection .. "}\\addtocounter{section}{-1}\\section{" .. titre .. "}"
end

function Reponses:subsection(nSubsection, titre)-- Ajoute une subsection
    Reponses.tempSubsection = "\\setcounter{subsection}{" .. nSubsection .. "}\\addtocounter{subsection}{-1}\\subsection{" .. titre .. "}"
end

function Reponses:exercice(nExercice, titre)-- Ajoute un exercice
    Reponses.tempExercice = "\\subsubsection*{Exercice " .. nExercice .. " - " .. titre .. "}"
end

function Reponses:reponse(nQuestion, nSubQuestion, reponse)-- Ajoute une réponse
    Reponses.chaine = Reponses.chaine .. Reponses.tempSection-- Si c'est la première réponse de la section, on valide l'ajout de la section dans la partie réponses
    Reponses.tempSection = ""
    Reponses.chaine = Reponses.chaine .. Reponses.tempSubsection-- Idem pour subsection
    Reponses.tempSubsection = ""
    Reponses.chaine = Reponses.chaine .. Reponses.tempExercice-- Idem pour exercice
    Reponses.tempExercice = ""
    Reponses.chaine = Reponses.chaine .. "\\par\\noindent" .. nQuestion .. ".\\tabto{1.4em}";-- Numéro de la question
    if nSubQuestion ~= "" then
      Reponses.chaine = Reponses.chaine .. "\\tabto{1.4em}" .. nSubQuestion .. ")\\tabto{2.7em}";-- Numéro de la sousquestion, éventuellement
    end
    Reponses.chaine = Reponses.chaine .. reponse;-- Ajout de la réponse, finalement
end

return Reponses

