# KERDOUD YASMINE

<img src="https://github.com/kerdoudyasmineencg-arch/DS-1/blob/main/Analyse%20Student%20Life%20%26%20Stress%20Factors/Yasmine%20kerdoud%20CAC2.jpg" style="height:464px;margin-right:432px"/>

# CAC2

# 22005999



# 📘 Compte Rendu – Remote Work & Mental Health

## 🎯 Objectif du Projet
L’objectif de cette analyse est d’étudier comment différents facteurs liés au travail à distance, hybride ou en présentiel influencent le **niveau de stress**, la **santé mentale**, l’**isolement social** et la **satisfaction professionnelle** des employés.  
À partir d’un dataset synthétique de 5 000 employés, l’objectif est donc de :
- comprendre les relations entre le mode de travail et le bien-être psychologique ;  
- identifier les variables les plus déterminantes du stress ;  
- construire un modèle prédictif capable d’estimer le **Stress_Level** (Low, Medium, High) ;  
- proposer une interprétation concrète des facteurs influençant le stress en milieu professionnel moderne.

Ce projet vise autant l’analyse exploratoire que la modélisation supervisée.

---

## 📊 Description du Dataset
Ce dataset contient **5 000 enregistrements synthétiques** simulant le comportement d’employés de différents secteurs et modes de travail.  
Il est entièrement artificiel mais reproduit des tendances plausibles liées au télétravail, permettant une analyse sans contraintes éthiques.

### Variables principales :
- **Employee_ID** : identifiant unique  
- **Age**, **Gender**  
- **Job_Role**, **Industry**  
- **Work_Location** : Remote / Hybrid / Onsite  
- **Stress_Level** : Low / Medium / High (variable cible)  
- **Mental_Health_Condition** : conditions simulées (anxiété, dépression…)  
- **Social_Isolation_Rating (1–5)**  
- **Satisfaction_with_Remote_Work** : Satisfied / Neutral / Unsatisfied  
- Indicateurs professionnels : heures travaillées, réunions virtuelles, équilibre vie pro/perso, soutien de l’entreprise…

Ces variables permettent une analyse combinant données démographiques, psychosociales et organisationnelles.

---

## 🔍 Approche Méthodologique
- Vérification et préparation des données numériques.  
- Séparation **train/test avant imputation** pour éviter le data leakage.  
- Imputation par moyenne uniquement sur le train.  
- Entraînement d’un **RandomForestClassifier (200 arbres)** sur les variables numériques.  
- Transformation de la cible en catégories numériques pour la classification.

---

## 📈 Résultats et Observations
- **Accuracy obtenue : 34.8%**  
  Cette performance est limitée par l’utilisation exclusive des variables numériques (absence d’encodage des variables catégorielles riches telles que Job_Role, Industry, Work_Location).

### Principaux facteurs influençant le stress :
1. Company_Support_for_Remote_Work  
2. Work_Life_Balance_Rating  
3. Social_Isolation_Rating  
4. Hours_Worked_Per_Week  
5. Number_of_Virtual_Meetings  

Les résultats montrent clairement que le stress est fortement influencé par :
- les facteurs psychosociaux (isolement, équilibre vie pro/perso),  
- les conditions organisationnelles (soutien, charge de travail).

---

## 🧠 Analyse et Interprétation
L’étude révèle que les aspects humains et organisationnels ont un impact plus fort sur le stress que les simples données démographiques.  
Le modèle actuel peine à classifier correctement les niveaux de stress car il n’intègre pas encore :
- les variables catégorielles (très informatives),  
- les interactions entre variables,  
- l’optimisation d’hyperparamètres.

---

## 🚀 Recommandations pour Amélioration
- Encoder toutes les variables catégorielles (One-Hot / Target Encoding).  
- Tester des modèles plus performants : **XGBoost**, **LightGBM**, **CatBoost**.  
- Réaliser une optimisation par **GridSearchCV** ou **RandomizedSearchCV**.  
- Ajouter des interactions et variables dérivées (Feature Engineering).  
- Étudier les erreurs du modèle pour cibler les zones d’ambiguïté.

---

## ✔️ Conclusion
Cette analyse met en évidence l’importance du mode de travail et des facteurs psychosociaux dans la compréhension du stress des employés.  
Bien que la première version du modèle obtienne une accuracy modeste (34.8%), les pistes d’amélioration identifiées permettront d’atteindre des performances nettement supérieures grâce à l’intégration complète des données disponibles.

Ce dataset synthétique constitue un excellent support pour explorer les liens entre télétravail, bien-être, performance et santé mentale en contexte professionnel.


