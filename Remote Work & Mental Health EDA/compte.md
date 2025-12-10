\documentclass[12pt]{report}
\usepackage{graphicx}
\usepackage{amsmath}
\usepackage{array}
\usepackage{geometry}
\usepackage{float}
\usepackage{setspace}
\usepackage{booktabs}

\geometry{a4paper, margin=1in}
\onehalfspacing

\begin{document}

\begin{titlepage}
\centering
{\Huge \textbf{Analyse Exploratoire du Dataset : Remote Work \& Mental Health}}\\[1cm]
{\Large Projet Data Science}\\[2cm]
{\large Étudiante : Yasmine}\\[0.5cm]
{\large Date : \today}
\end{titlepage}

\tableofcontents
\newpage

%---------------------------------------------------------
\chapter{Introduction}

\section{Contexte}
Le télétravail s'est rapidement imposé comme une transformation majeure dans les environnements professionnels. 
Cette nouvelle organisation du travail influence la santé mentale, les niveaux de stress, l’isolement social et la satisfaction des employés.

L’objectif de ce projet est de mener une analyse exploratoire (EDA) d’un dataset synthétique contenant 5000 observations générées artificiellement, dans le but de :
\begin{itemize}
    \item comprendre l’impact du télétravail (Remote, Hybrid, Onsite),
    \item explorer les liens entre stress, santé mentale et satisfaction,
    \item identifier des tendances utiles pour la recherche ou les RH.
\end{itemize}

Ce travail se concentre uniquement sur l’exploration des données (EDA) et ne vise pas la prise de décisions réelles, car le dataset n’est pas issu du monde réel.

%---------------------------------------------------------
\chapter{Description du Dataset}

Le dataset contient 5000 employés synthétiques. Chaque ligne représente un individu et chaque colonne une caractéristique professionnelle ou psychologique.

\section{Variables}
Voici les principales variables :

\begin{itemize}
    \item \textbf{Employee\_ID} : Identifiant unique.
    \item \textbf{Age} : Âge de l'employé.
    \item \textbf{Gender} : Homme, Femme ou Autres.
    \item \textbf{Job\_Role} : Fonction professionnelle.
    \item \textbf{Industry} : Secteur d’activité.
    \item \textbf{Work\_Location} : Remote, Hybrid ou Onsite.
    \item \textbf{Stress\_Level} : Low, Medium, High.
    \item \textbf{Mental\_Health\_Condition} : Anxiety, Depression, None, etc.
    \item \textbf{Social\_Isolation\_Rating} : Score de 1 à 5.
    \item \textbf{Satisfaction\_with\_Remote\_Work} : Satisfied, Neutral, Unsatisfied.
\end{itemize}

Ces variables couvrent trois dimensions essentielles :
\begin{enumerate}
    \item Professionnelle (Job Role, Industry, Work Location)
    \item Psychologique (Stress Level, Mental Health Condition)
    \item Sociale (Isolation Rating, Satisfaction)
\end{enumerate}

%---------------------------------------------------------
\chapter{Méthodologie}

\section{Importation des Données}
Les données ont été importées avec \texttt{pandas} :

\begin{verbatim}
df = pd.read_csv("Dataset.csv")
\end{verbatim}

Aucune donnée manquante n'était présente dans le dataset.

\section{Préparation des Données}
Les étapes suivantes ont été appliquées :
\begin{itemize}
    \item conversion des types (catégoriels vs numériques),
    \item vérification des doublons,
    \item construction d’un DataFrame propre pour l’EDA,
    \item exploration des distributions de chaque variable.
\end{itemize}

\section{Objectifs de l’EDA}
\begin{itemize}
    \item étudier les tendances des niveaux de stress selon le mode de travail,
    \item analyser la relation entre isolement social et télétravail,
    \item comprendre comment les conditions de santé mentale varient selon les catégories professionnelles,
    \item observer la satisfaction vis-à-vis du travail à distance.
\end{itemize}

%---------------------------------------------------------
\chapter{Analyse Exploratoire (EDA)}

\section{Distribution des Modes de Travail}
L'analyse montre que les employés sont répartis sur trois catégories :
\begin{itemize}
    \item Remote : proportion importante dans les secteurs technologiques,
    \item Hybrid : modèle dominant dans la majorité des industries,
    \item Onsite : secteurs traditionnels ou nécessitant une présence physique.
\end{itemize}

\section{Stress des Employés}
Une étude croisée révèle :
\begin{itemize}
    \item Le stress est légèrement plus élevé chez les employés \textbf{onsite}.
    \item Les travailleurs \textbf{remote} déclarent un stress souvent \textbf{medium}.
    \item Les travailleurs \textbf{hybrid} présentent la répartition la plus équilibrée.
\end{itemize}

\section{Santé Mentale}
On note :
\begin{itemize}
    \item L’anxiété est plus fréquente chez les employés entièrement en télétravail.
    \item La dépression apparaît davantage dans les environnements onsite.
\end{itemize}

\section{Isolement Social}
Les scores moyens montrent :
\begin{itemize}
    \item Remote : isolement plus élevé (score souvent 4 ou 5).
    \item Hybrid : score modéré.
    \item Onsite : score faible, forte interaction sociale.
\end{itemize}

\section{Satisfaction vis-à-vis du Travail à Distance}
Globalement, les travailleurs remote sont les plus satisfaits, tandis que les onsite sont les moins satisfaits.

%---------------------------------------------------------
\chapter{Visualisations}

Les graphiques suivants ont été générés dans le notebook (exemples mentionnés dans le rapport) :

\begin{itemize}
    \item Histogrammes des âges.
    \item Countplots des niveaux de stress.
    \item Heatmap des corrélations entre variables numériques.
    \item Boxplots du score d’isolement selon le mode de travail.
    \item Diagramme en barres pour la satisfaction du travail à distance.
\end{itemize}

Chaque visualisation a permis de valider ou d’affiner les observations décrites dans l’analyse exploratoire.

%---------------------------------------------------------
\chapter{Interprétation et Discussion}

\section{Impact du Télétravail}
Le télétravail n’améliore pas nécessairement la santé mentale : 
\begin{itemize}
    \item il augmente la satisfaction,
    \item mais aussi l’isolement,
    \item et favorise les conditions comme l’anxiété.
\end{itemize}

\section{Importance du Mode Hybrid}
Le mode Hybrid apparaît comme un compromis optimal :
\begin{itemize}
    \item stress plus stable,
    \item isolement modéré,
    \item satisfaction acceptable.
\end{itemize}

\section{Limites}
Comme les données sont synthétiques :
\begin{itemize}
    \item les résultats ne doivent pas être généralisés au monde réel,
    \item certaines corrélations peuvent refléter des choix de génération artificielle.
\end{itemize}

%---------------------------------------------------------
\chapter{Conclusion}

Ce projet a permis une exploration approfondie des liens entre organisation du travail et bien-être professionnel.  
L’EDA met en évidence des tendances cohérentes avec la littérature :
\begin{itemize}
    \item le télétravail améliore la satisfaction,
    \item il augmente l’isolement social,
    \item le stress varie selon les secteurs et les rôles,
    \item le modèle hybrid semble le plus équilibré.
\end{itemize}

Ce travail constitue une base solide pour des analyses plus avancées, comme la prédiction du stress ou la modélisation de la satisfaction au travail.

\end{document}
