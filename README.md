# 📍 Application Géospatiale Interactive

Ce projet est une application interactive développée avec **Streamlit** et **Folium**, permettant la visualisation et l'analyse de données géospatiales sur une carte dynamique. L'application inclut des filtres multicritères et une option de téléchargement des données filtrées.

## 🚀 Fonctionnalités
- 📌 **Affichage d'une carte interactive** avec des marqueurs représentant les groupements agricoles.
- 🔍 **Filtres dynamiques** pour sélectionner les données par :
  - Milieu de résidence (urbain, rural, périurbain)
  - Sexe des membres
  - Tranche d'âge
  - Type de groupement
  - Activités menées (production, transformation, commercialisation, etc.)
- 📊 **Affichage des données filtrées** sous forme de tableau interactif.
- 📥 **Téléchargement des données filtrées** en format CSV.

## 🛠️ Technologies Utilisées
- **Python** (Langage principal)
- **Streamlit** (Interface utilisateur interactive)
- **Folium** (Cartographie interactive)
- **Pandas** (Traitement et manipulation des données)
- **Streamlit-Folium** (Intégration de Folium dans Streamlit)

## 📂 Structure du Projet
```
📁 MonProjetGeo
│── 📄 app.py             # Code de l'application
│── 📊 BDD_geospatiale_04032025.xlsx  # Base de données
│── 📜 README.md          # Ce fichier
```

## 📌 Installation et Exécution

### 1️⃣ Installer les bibliothèques requises
Exécutez la commande suivante pour installer les dépendances :
```bash
pip install streamlit pandas folium openpyxl streamlit-folium
```

### 2️⃣ Lancer l'application
Naviguez dans le dossier du projet et exécutez :
```bash
streamlit run app.py
```
L'application s'ouvrira automatiquement dans votre navigateur.

## 🛠️ Déploiement
### 🚀 Déploiement sur Streamlit Cloud
1. **Créer un dépôt GitHub** et y ajouter tous les fichiers du projet.
2. **Se connecter à [Streamlit Cloud](https://streamlit.io/)**.
3. **Déployer l'application** en sélectionnant votre dépôt GitHub.
4. **Obtenir un lien public** et le partager avec les utilisateurs.

## 📌 Problèmes Courants et Solutions

### ❌ Fichier Excel introuvable
**Erreur** : `FileNotFoundError: No such file or directory: 'BDD_geospatiale_04032025.xlsx'`

✅ **Solution** :
- Vérifiez que le fichier Excel est bien dans le dossier du projet.
- Modifiez `file_path` dans `app.py` avec le chemin absolu si nécessaire.

### ❌ Module Folium introuvable
**Erreur** : `ModuleNotFoundError: No module named 'folium'`

✅ **Solution** :
```bash
pip install folium streamlit-folium
```

## 🎯 Améliorations Futures
✔️ Personnalisation des couleurs et icônes des marqueurs.
✔️ Ajout de statistiques et graphiques interactifs.
✔️ Intégration d'une base de données pour une gestion avancée.

## 📬 Contact
Si vous avez des questions ou suggestions, n'hésitez pas à me contacter ! 🚀
