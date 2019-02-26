Reponses = {chaine = "", tempExercice = "", tempSubsection = "", tempSection = ""}

function Reponses:reponse(nQuestion, nSubQuestion, reponse)
    Reponses.chaine = Reponses.chaine .. Reponses.tempSection
    Reponses.tempSection = ""
    Reponses.chaine = Reponses.chaine .. Reponses.tempSubsection
    Reponses.tempSubsection = ""
    Reponses.chaine = Reponses.chaine .. Reponses.tempExercice
    Reponses.tempExercice = ""
    Reponses.chaine = Reponses.chaine .. "\\par\\noindent" .. nQuestion .. ".\\tabto{1.4em}";
    if nSubQuestion ~= "" then
      Reponses.chaine = Reponses.chaine .. "\\tabto{1.4em}" .. nSubQuestion .. ")\\tabto{2.7em}";
    end
    Reponses.chaine = Reponses.chaine .. reponse;
end

function Reponses:exercice(nExercice, titre)
    Reponses.tempExercice = "\\subsubsection*{Exercice " .. nExercice .. " - " .. titre .. "}"
end

function Reponses:subsection(nSubsection, titre)
    Reponses.tempSubsection = "\\setcounter{subsection}{" .. nSubsection .. "}\\addtocounter{subsection}{-1}\\subsection{" .. titre .. "}"
end

function Reponses:section(nSection, titre)
    Reponses.tempSection = "\\setcounter{section}{" .. nSection .. "}\\addtocounter{section}{-1}\\section{" .. titre .. "}"
end

return Reponses

