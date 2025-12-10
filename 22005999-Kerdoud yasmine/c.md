# KERDOUD YASMINE

<img src="https://github.com/kerdoudyasmineencg-arch/DS-1/blob/main/Analyse%20Student%20Life%20%26%20Stress%20Factors/Yasmine%20kerdoud%20CAC2.jpg" style="height:464px;margin-right:432px"/>

# CAC2

# 22005999

# RCompte-rendu : Impact du Télétravail sur la Santé Mentale et la Satisfaction des Employés

---

## 1. Contexte Métier et Mission

### Le Problème Métier  
La généralisation du **travail à distance** a profondément transformé les environnements professionnels. Les organisations cherchent désormais à comprendre :

- Comment le télétravail influence **la santé mentale**,  
- Quel est son impact sur **la productivité**,  
- Comment il affecte **la satisfaction**, **le stress**, et **l’équilibre vie pro/vie perso**.

L’objectif principal est d'apporter une vision claire permettant aux équipes RH et aux dirigeants de prendre des décisions éclairées liées à la politique de travail hybride ou à distance.

### Mission du Projet  
Réaliser une **Analyse Exploratoire des Données (EDA)** afin d’étudier les tendances majeures et les relations entre variables :

- Lieu de travail (Remote, Hybrid, Onsite)
- Stress et santé mentale
- Satisfaction au travail
- Productivité
- Engagement social

### L’Enjeu Critique  
Une mauvaise politique de travail peut :

- Augmenter le stress et le burnout,  
- Diminuer la satisfaction et la performance,  
- Aggraver la santé mentale des employés,  
- Impacter directement la rétention et la productivité globale.

Les résultats de cette étude ont donc un **impact stratégique** sur les décisions RH.

---

## 2. Le Code Python (Laboratoire)

Le script Python fourni réalise :

1. **Chargement du dataset** (5 000 employés générés de manière synthétique).  
2. **Inspection des données** : `head()`, `info()`, valeurs manquantes.  
3. **Visualisations** :
   - Distribution d’âge  
   - Répartition du genre  
   - Répartition des rôles et industries  
   - Work Location vs Productivity Change  
   - Satisfaction avec les années d'expérience  
   - Conditions de santé mentale  
   - Heatmap des corrélations  
4. **Analyse relationnelle** via 2D et 3D scatter plots.

Ce script constitue un **laboratoire complet d’EDA** permettant de comprendre la structure du dataset avant tout modèle prédictif.

---

## 3. Analyse Approfondie des Données

### 3.1 Compréhension du Dataset  
Le dataset contient 5 000 enregistrements synthétiques simulant un environnement de travail moderne.

| Colonne | Description |
|--------|-------------|
| Age | Âge de l’employé |
| Gender | Genre |
| Job_Role | Poste |
| Industry | Secteur d’activité |
| Work_Location | Remote, Hybrid, Onsite |
| Stress_Level | Low, Medium, High |
| Mental_Health_Condition | Anxiety, Depression, None |
| Social_Isolation_Rating | Score de 1 à 5 |
| Satisfaction_with_Remote_Work | Satisfied, Neutral, Unsatisfied |

Ce dataset est destiné à l’analyse RH, aux études statistique ou à la construction de modèles prédictifs.

---

### 3.2 Nettoyage des Données  
Le script vérifie les valeurs manquantes via `df.isnull().sum()`.  
Aucune valeur manquante significative n’est détectée, ce qui :

- facilite l’analyse,  
- évite les stratégies d’imputation,  
- garantit la stabilité statistique des visualisations.

Les données étant synthétiques, elles sont **propres et cohérentes**, ce qui est courant dans les datasets générés à des fins pédagogiques.

---

## 4. Interprétation des Graphiques Clés  
Voici les **trois visualisations les plus importantes**, choisies pour leur impact stratégique et analytique.

---

### **Graphique 1 — Satisfaction with Remote Work vs Years of Experience (Boxplot)**
<img src="https://github.com/kerdoudyasmineencg-arch/DS-1/blob/main/22005999-Kerdoud%20yasmine/Graphique%201.png" style="height:464px;margin-right:432px"/>

#### Interprétation
Ce graphique montre comment la satisfaction varie selon l’expérience professionnelle.

**Tendances observées :**

- Les employés **moins expérimentés** semblent plus satisfaits du télétravail.  
- Les employés avec **plus d’années d’expérience** montrent une satisfaction plus variée (dispersion plus large).  
- Les seniors semblent parfois **moins satisfaits**, probablement à cause :
  - d’un besoin plus fort de contact direct,  
  - d’habitudes de travail classiques,  
  - ou de responsabilités nécessitant des interactions physiques.

#### Insights Métiers
- Les politiques RH doivent être **adaptées par tranche d’expérience**.  
- Le télétravail peut être un **levier d’attractivité pour les jeunes talents**.

---

### **Graphique 2 — Work Location vs Productivity Change**
<img src="https://github.com/kerdoudyasmineencg-arch/DS-1/blob/main/22005999-Kerdoud%20yasmine/Graphique%202.png" style="height:464px;margin-right:432px"/>

#### Interprétation
Ce graphique présente la relation entre le lieu de travail et l’évolution de la productivité.

**Résultats généraux :**

- Les employés **remote** montrent souvent une productivité stable ou légèrement accrue, probablement grâce à :
  - moins de distractions,  
  - flexibilité accrue,  
  - optimisation du temps.  

- Les employés **hybrid** se situent entre les deux extrêmes.  
- Les employés **onsite** montrent parfois une productivité plus hétérogène.

#### Insights Métiers
- Le télétravail **n’est pas synonyme de baisse de performance**.  
- Le modèle hybride semble offrir un **compromis intéressant**.  
- Les entreprises doivent analyser les tâches nécessitant réellement une présence physique.

---

### **Graphique 3 — Heatmap des Corrélations**
<img src="https://github.com/kerdoudyasmineencg-arch/DS-1/blob/main/22005999-Kerdoud%20yasmine/Graphique%203.png"/>

#### Interprétation
Cette visualisation montre les relations entre variables numériques (âge, isolation, satisfaction…).

**Observations majeures :**

- Une corrélation notable entre **Social Isolation Rating** et **Stress Level** :  
  → Plus l’isolement social augmente, plus le stress est élevé.

- Une corrélation inverse potentielle entre **Satisfaction_with_Remote_Work** et certains indicateurs de stress ou d’isolement.  

- L’âge influence légèrement :
  - le stress,  
  - la satisfaction,  
  - le niveau d’activité professionnelle.

#### Insights Métiers
- L’isolement social est **un facteur critique à surveiller en télétravail**.  
- Les entreprises doivent mettre en place :
  - des réunions régulières,  
  - des activités d’équipe virtuelles,  
  - des programmes de bien-être.

---

## 5. Synthèse Globale et Recommandations

### Ce que révèle l’analyse :
- Le télétravail **peut améliorer la satisfaction**, surtout pour les employés juniors.  
- La productivité **ne baisse pas** avec le remote, et peut même augmenter.  
- L’isolement social est **le principal risque** du télétravail, impactant le stress et la santé mentale.  
- Le modèle hybride semble représenter un **équilibre optimal**.

### Recommandations RH :
1. **Adapter les politiques selon l’expérience.**  
2. **Renforcer les programmes anti-isolement.**  
3. **Former les managers à la gestion d’équipes hybrides.**  
4. **Suivre régulièrement les indicateurs de santé mentale.**

---

## 6. Conclusion  
Cette étude met en évidence que le télétravail est loin d’être une menace pour la performance ou la satisfaction. Il peut au contraire constituer un **levier de bien-être**, à condition d’être encadré correctement.

L’analyse permet d’identifier les **facteurs clés** à surveiller :  
- l’isolement,  
- l’expérience professionnelle,  
- l’adéquation travail ↔ lieu de travail.

Ce rapport fournit donc une base solide pour optimiser les politiques RH dans un contexte de travail flexible.

---
