# Compte-rendu d'analyse du dataset (version corrigée)

Analyse faite en respectant la séparation train/test avant imputation pour éviter la fuite de données. Référence méthodologique : Correction Projet. fileciteturn1file0

- Observations : 5000
- Features numériques utilisées pour le modèle : 7
- Colonne cible : Stress_Level


## Résultats clés

- Accuracy (test) : **34.80%**


### Rapport détaillé

|              |   precision |   recall |   f1-score |   support |
|:-------------|------------:|---------:|-----------:|----------:|
| 0            |    0.346041 | 0.350148 |   0.348083 |   337     |
| 1            |    0.342618 | 0.37386  |   0.357558 |   329     |
| 2            |    0.356667 | 0.320359 |   0.337539 |   334     |
| accuracy     |    0.348    | 0.348    |   0.348    |     0.348 |
| macro avg    |    0.348442 | 0.348123 |   0.347727 |  1000     |
| weighted avg |    0.348464 | 0.348    |   0.347679 |  1000     |

### Matrice de confusion

![Matrice de confusion](/mnt/data/confusion_matrix.png)


### Top features

|                                 |         0 |
|:--------------------------------|----------:|
| Hours_Worked_Per_Week           | 0.197611  |
| Age                             | 0.196963  |
| Years_of_Experience             | 0.192577  |
| Number_of_Virtual_Meetings      | 0.152782  |
| Company_Support_for_Remote_Work | 0.0917713 |
| Work_Life_Balance_Rating        | 0.0851422 |
| Social_Isolation_Rating         | 0.0831538 |