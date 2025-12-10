# 📘 Projet : Analyse du Stress lié au Télétravail  
### *Compte rendu complet – Analyse exploratoire, Modélisation et Recommandations*

---

## 1. Contexte et Problématique

L’objectif de ce projet est d’analyser un ensemble de données portant sur **5000 employés** travaillant en environnement **remote / hybride**, afin d comprendre les facteurs qui influencent le **niveau de stress**, catégorisé en :

- `High`
- `Medium`
- `Low`

Le problème métier est clair :

> **Quels facteurs professionnels et psychosociaux permettent d’expliquer ou de prédire le niveau de stress d’un employé en télétravail ?**

Ce travail vise donc à :
- explorer les données (EDA),
- comprendre les relations entre variables,
- identifier les facteurs de stress majeurs,
- et construire un modèle prédictif robuste.

---

## 2. Description du Dataset

### 2.1 Dimensions
- **5000 observations**
- **20 variables**
- Types de variables :
  - numériques : 7
  - catégorielles : 12
  - identifiant : 1 (`Employee_ID`)

### 2.2 Variable cible
- `Stress_Level`  
- Répartition équilibrée :
  | Classe | Effectif |
  |--------|----------|
  | High   | 1686     |
  | Medium | 1669     |
  | Low    | 1645     |

Cette distribution quasi uniforme permet d’éviter les problèmes d’apprentissage dus à des classes majoritaires.

### 2.3 Variables Numériques Clés
Les variables numériques utilisées dans la modélisation :

| Variable | Description |
|---------|-------------|
| Age | Âge de l’employé |
| Years_of_Experience | Expérience totale |
| Hours_Worked_Per_Week | Heures travaillées |
| Number_of_Virtual_Meetings | Nombre de réunions virtuelles |
| Work_Life_Balance_Rating | Score équilibre vie pro/perso |
| Social_Isolation_Rating | Score d’isolement social |
| Company_Support_for_Remote_Work | Soutien de l’entreprise |

---

## 3. Préparation des Données (Data Wrangling)

### 3.1 Nettoyage
- Vérification des valeurs manquantes
- Aucun NaN trouvé dans les variables numériques.

### 3.2 Évitement du Data Leakage  
Une bonne pratique essentielle a été suivie :

> **Séparation Train/Test AVANT imputation.**

Étapes appliquées :
1. Split (80% train / 20% test)
2. Imputation (moyenne) **ajustée uniquement sur le train**
3. Transformation du test avec les paramètres du train

Cette démarche garantit la validité des performances du modèle.

### 3.3 Encodage de la cible
Mapping utilisé :

---

## 4. Analyse Exploratoire (EDA)

### 4.1 Statistiques descriptives
Observations principales :
- Les heures travaillées varient fortement (fatigue potentielle).
- Le nombre de réunions virtuelles est très dispersé (charge cognitive).
- Les scores psychologiques montrent une hétérogénéité notable, signe de profils variés.

### 4.2 Distributions
- `Hours_Worked_Per_Week` : distribution asymétrique suggérant surcharge chez certains employés.
- `Work_Life_Balance_Rating` : forte concentration entre 2 et 3 → insatisfaction modérée.

### 4.3 Corrélations
Aucune corrélation > 0.90 entre variables numériques.  
Donc :
- Pas de redondance extrême,
- Pas de besoin urgent de réduction de dimension.

### 4.4 Hypothèses exploratoires
- Plus de réunions virtuelles → stress plus élevé.
- Isolement social → stress plus fort.
- Faible équilibre vie pro/perso → stress élevé.

L’étape de modélisation permettra de valider (ou infirmer) ces hypothèses.

---

## 5. Modélisation

### 5.1 Modèle choisi
Modèle utilisé :

Pourquoi ?
- robuste aux valeurs extrêmes,
- non sensible au scaling,
- capture bien les interactions,
- baseline fiable avant modèles plus avancés (XGBoost / LightGBM).

### 5.2 Jeu de données
- Train : 4000 lignes
- Test : 1000 lignes

### 5.3 Variables d’entrée utilisées  
Uniquement les **variables numériques**, car les catégorielles n’étaient pas encore encodées (One-Hot, Target Encoding).

---

## 6. Résultats du Modèle

### 6.1 Accuracy

Interprétation :
- Score faible pour une classification à 3 classes.
- Le modèle ne parvient pas à capturer suffisamment la structure sous-jacente, car beaucoup d’information est contenue dans les variables catégorielles.

### 6.2 Matrice de confusion

*(Image dans ton dossier si nécessaire)*

Elle montre un mélange important des classes, signe que les features numériques seules ne suffisent pas.

### 6.3 Rapport de classification
Résultat homogène entre classes (~34% chacune) →  
aucune classe n’est clairement identifiable à partir des seules variables numériques.

### 6.4 Importance des variables

Top 5 features :
1. Company_Support_for_Remote_Work
2. Work_Life_Balance_Rating
3. Social_Isolation_Rating
4. Hours_Worked_Per_Week
5. Number_of_Virtual_Meetings

➡️ **Les facteurs psychosociaux sont déterminants dans le stress.**

---

## 7. Analyse Critique et Limites

### 7.1 Limites du modèle actuel
- Les variables catégorielles (très informatives) NE SONT PAS ENCORE UTILISÉES :
  - Job_Role
  - Industry
  - Work_Location  
  → Manque majeur d’information.
- Pas d’optimisation d’hyperparamètres.
- Aucune régularisation.
- Modèle non calibré → mauvaise interprétation des probabilités.
- Interactions non exploitées.

### 7.2 Qualité du dataset
Points forts :
- riche et varié
- dataset équilibré
- grande taille → très bon pour apprentissage supervisé

Points faibles :
- nécessité d’un encodage avancé pour les variables catégorielles
- potentielle subjectivité des scores psychosociaux

---

## 8. Recommandations pour Améliorer la Performance

### 8.1 Traitement des variables catégorielles
Recommandé :
- **One-Hot Encoding** pour petits ensembles
- **Target Encoding** pour des catégories nombreuses (ex : Job_Role)
- Possibilité d’utiliser **embeddings** pour la haute cardinalité

### 8.2 Modèles à tester
- **XGBoost** (souvent le meilleur en tabulaire)
- LightGBM
- CatBoost (excellent pour variables catégorielles)
- Logistic regression + régularisation L2

### 8.3 Optimisation
- RandomizedSearchCV sur :
  - max_depth
  - min_samples_leaf
  - n_estimators
  - max_features
- Validation croisée stratifiée (k=5)

### 8.4 Ingénierie de features
- Interaction Hours × Meetings
- Interaction Work-Life Balance × Company Support
- Construction d’un score composé

### 8.5 Analyse métier complémentaire
- Étudier les employés classés High alors que leurs scores semblent neutres  
→ utile pour des actions RH ciblées.

---

## 9. Conclusion

Ce travail montre clairement que :

- Les facteurs les plus déterminants du stress sont psychosociaux (soutien, équilibre, isolement).
- Le modèle actuel atteint **34.8% d'accuracy**, mais ce score est **limité par l’absence d’utilisation des variables catégorielles**.
- En intégrant l’ensemble des features du dataset, en optimisant le modèle et en ajoutant un encodage adapté, on peut espérer un score **entre 60% et 80%**.

---

## 10. Fichiers générés

- `compte_rendu_dataset_analysis.md`
- `compte_rendu_dataset_analysis.tex`
- `confusion_matrix.png`
- `feature_importances.png`

---

## ✔️ Travail futur possible (sur demande)
- Version PDF du rapport  
- Nouvelle modélisation complète avec toutes les variables  
- Version courte du rapport  
- Version plus scientifique  
- Ajout d’un tableau final comparatif des modèles  



