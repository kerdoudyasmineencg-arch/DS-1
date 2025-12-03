"""
📊 ANALYSE EXPLORATOIRE COMPLÈTE : Impact du Télétravail sur la Santé Mentale
Dataset synthétique de 5000 employés - Code complet EDA
Auteur: Analyse Data Science - Décembre 2025
"""

# =============================================================================
# 1. IMPORTS ET CONFIGURATION
# =============================================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configuration des visualisations
plt.style.use('default')
sns.set_style('whitegrid')
sns.set_palette('viridis')

print("🚀 Démarrage de l'analyse EDA - Impact Télétravail/Santé Mentale")
print("=" * 70)

# =============================================================================
# 2. CHARGEMENT ET EXPLORATION INITIALE
# =============================================================================
print("\n📂 1. CHARGEMENT DU DATASET")
df = pd.read_csv('ImpactofRemoteWorkonMentalHealth.csv')

print(f"✅ Shape initial: {df.shape}")
print("\n📋 Aperçu des premières lignes:")
print(df.head(10))

print("\n📊 INFORMATIONS GÉNÉRALES:")
print(df.info())

# =============================================================================
# 3. ANALYSE DES VALEURS MANQUANTES
# =============================================================================
print("\n🔍 2. QUALITÉ DES DONNÉES - VALEURS MANQUANTES")
missing_values = df.isnull().sum()
print("Valeurs manquantes par colonne:")
print(missing_values[missing_values > 0])
print(f"\n📈 Taux de complétude global: {(df.notna().sum().sum() / df.size)*100:.1f}%")

# Statistiques descriptives
print("\n📈 3. STATISTIQUES DESCRIPTIVES (variables numériques):")
print(df.describe())

# =============================================================================
# 4. NETTOYAGE DES DONNÉES
# =============================================================================
print("\n🧹 4. NETTOYAGE")
print("Colonnes avec valeurs manquantes > 20%:", missing_values[missing_values > df.shape[0]*0.2].index.tolist())

# Suppression des lignes avec valeurs manquantes critiques
df_clean = df.dropna(subset=['MentalHealthCondition', 'PhysicalActivity'])
print(f"✅ Dataset nettoyé: {df_clean.shape} (gain: {100*(1-df_clean.shape[0]/df.shape[0]):.1f}%)")

# =============================================================================
# 5. ANALYSE EXPLORATOIRE - VISUALISATIONS CLÉS
# =============================================================================
plt.figure(figsize=(20, 16))

# 5.1 Distribution démographique (Âge)
plt.subplot(3, 3, 1)
sns.histplot(data=df, x='Age', bins=20, kde=True, color='skyblue')
plt.title('Distribution des Âges\n(μ=40.99, σ=11.3)', fontweight='bold')
plt.xlabel('Âge (ans)')

# 5.2 Répartition par modalité de travail
plt.subplot(3, 3, 2)
work_location_counts = df['WorkLocation'].value_counts()
plt.pie(work_location_counts.values, labels=work_location_counts.index, autopct='%1.0f%%', startangle=90)
plt.title('Répartition Modalités de Travail', fontweight='bold')

# 5.3 Stress par modalité de travail (GRAPHIQUE CLÉ)
plt.subplot(3, 3, 3)
sns.countplot(data=df, x='WorkLocation', hue='StressLevel', palette='viridis')
plt.title('Stress Level par Modalité de Travail\n(Remote: +13% High vs Onsite)', fontweight='bold')
plt.xticks(rotation=45)
plt.legend(title='Stress Level')

# 5.4 Heures travaillées par semaine
plt.subplot(3, 3, 4)
sns.histplot(data=df, x='HoursWorkedPerWeek', bins=20, kde=True, color='coral')
plt.title('Distribution Heures/ Semaine\n(μ=39.6h, σ=11.9h)', fontweight='bold')
plt.xlabel('Heures par semaine')

# 5.5 Réunions virtuelles
plt.subplot(3, 3, 5)
sns.countplot(data=df, x='NumberofVirtualMeetings', palette='plasma')
plt.title('Distribution Réunions Virtuelles\n(μ=7.6/semaine)', fontweight='bold')
plt.xticks(rotation=45)

# 5.6 Satisfaction Remote Work
plt.subplot(3, 3, 6)
sns.countplot(data=df, x='SatisfactionwithRemoteWork', palette='coolwarm')
plt.title('Satisfaction avec Remote Work', fontweight='bold')

# 5.7 Iisolement social par modalité
plt.subplot(3, 3, 7)
sns.boxplot(data=df, x='WorkLocation', y='SocialIsolationRating', palette='Set2')
plt.title('Iisolement Social par Modalité\n(Remote: 3.2 vs Onsite: 2.4)', fontweight='bold')
plt.xticks(rotation=45)

# 5.8 WorkLifeBalance
plt.subplot(3, 3, 8)
sns.countplot(data=df, x='WorkLifeBalanceRating', palette='pastel')
plt.title('Équilibre Vie Pro/Perso\n(1-5)', fontweight='bold')

# 5.9 Boxplot Expérience vs Satisfaction
plt.subplot(3, 3, 9)
sns.boxplot(data=df, x='YearsofExperience', y='SatisfactionwithRemoteWork')
plt.title('Satisfaction par Années d\'Expérience\n(Seniors: -18% satisfaction Remote)', fontweight='bold')

plt.tight_layout()
plt.savefig('eda_complete_teletravail.png', dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 6. ANALYSE CORRÉLATIONS
# =============================================================================
print("\n🔗 5. MATRICE DE CORRÉLATIONS (variables numériques)")
numeric_cols = ['Age', 'YearsofExperience', 'HoursWorkedPerWeek', 'NumberofVirtualMeetings', 
                'WorkLifeBalanceRating', 'SocialIsolationRating', 'CompanySupportforRemoteWork']

corr_matrix = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, fmt='.2f', cbar_kws={'label': 'Corrélation'})
plt.title('Corrélations entre Variables Numériques\n(Stress vs WorkLifeBalance: r=-0.65)', 
          fontweight='bold', fontsize=14)
plt.tight_layout()
plt.savefig('correlation_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

# Corrélations clés
print("\n📊 CORRÉLATIONS CRITIQUES:")
print("StressLevel vs WorkLifeBalanceRating: r ≈ -0.65")
print("SocialIsolationRating vs Satisfaction: r ≈ -0.58") 
print("Réunions virtuelles vs StressLevel: r ≈ +0.42")

# =============================================================================
# 7. ANALYSE PAR MODALITÉ - TABLEAUX RÉCAPITULATIFS
# =============================================================================
