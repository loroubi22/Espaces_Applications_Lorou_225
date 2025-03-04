import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

# Charger les données
@st.cache_data
def load_data():
    import os
file_path = os.path.join(os.getcwd(), "BDD_geospatiale_04032025.xlsx")
df = pd.read_excel(file_path, sheet_name="Feuil1")

 # Remplacez par le bon chemin
    df = pd.read_excel(file_path, sheet_name="Feuil1")
    return df

df = load_data()

# Titre de l'application
st.title("📍 Application Géospatiale Interactive")

# **Filtres multicritères**
st.sidebar.header("🔍 Filtres")

# Filtres dynamiques
milieu = st.sidebar.multiselect("Milieu de résidence", df["Milieu"].unique())
sexe = st.sidebar.multiselect("Sexe", df["B2_sexe"].unique())
age = st.sidebar.multiselect("Tranche d'âge", df["B3_Age"].unique())
groupement = st.sidebar.multiselect("Nom du groupement", df["C1_Groupement"].unique())
activites = {
    "Production Agricole": "Prod_Agricole",
    "Transformation Agricole": "Transformation_Agricole",
    "Commercialisation": "C5_Commercialisation_Agricole",
    "Collecte et Commercialisation": "C5_Collecte_Commercialisation_Ag",
    "Formation Chaîne Valeurs": "C5_Formation_Chaine_Valeurs",
    "Financement AVEC": "C5_Financement_AVEC",
    "Unité de Transformation Manioc": "C6_Unite_Transformation_Manioc",
}
activite_choisie = st.sidebar.multiselect("Activité menée", activites.keys())

# Appliquer les filtres
filtered_df = df.copy()
if milieu:
    filtered_df = filtered_df[filtered_df["Milieu"].isin(milieu)]
if sexe:
    filtered_df = filtered_df[filtered_df["B2_sexe"].isin(sexe)]
if age:
    filtered_df = filtered_df[filtered_df["B3_Age"].isin(age)]
if groupement:
    filtered_df = filtered_df[filtered_df["C1_Groupement"].isin(groupement)]
if activite_choisie:
    cols = [activites[act] for act in activite_choisie]
    filtered_df = filtered_df[(filtered_df[cols] == "Oui").any(axis=1)]

# **Carte interactive**
st.subheader("🗺️ Carte Interactive")

# Création de la carte Folium
map_center = [filtered_df["GPS_latitude"].mean(), filtered_df["GPS_longitude"].mean()]
m = folium.Map(location=map_center, zoom_start=7)
marker_cluster = MarkerCluster().add_to(m)

# Ajouter les points
for _, row in filtered_df.iterrows():
    popup_info = (
        f"<b>Groupement:</b> {row['C1_Groupement']}<br>"
        f"<b>Milieu:</b> {row['Milieu']}<br>"
        f"<b>Sexe:</b> {row['B2_sexe']}<br>"
        f"<b>Tranche d'âge:</b> {row['B3_Age']}<br>"
        f"<b>Production Agricole:</b> {row['Prod_Agricole']}<br>"
        f"<b>Transformation Agricole:</b> {row['Transformation_Agricole']}<br>"
        f"<b>Commercialisation:</b> {row['C5_Commercialisation_Agricole']}<br>"
        f"<b>Collecte & Commercialisation:</b> {row['C5_Collecte_Commercialisation_Ag']}<br>"
        f"<b>Formation Chaine Valeurs:</b> {row['C5_Formation_Chaine_Valeurs']}<br>"
        f"<b>Financement AVEC:</b> {row['C5_Financement_AVEC']}<br>"
        f"<b>Unité Transformation Manioc:</b> {row['C6_Unite_Transformation_Manioc']}<br>"
    )

    folium.Marker(
        location=[row["GPS_latitude"], row["GPS_longitude"]],
        popup=folium.Popup(popup_info, max_width=300),
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(marker_cluster)

# Affichage de la carte
folium_static(m)

# **Affichage des données filtrées**
st.subheader("📋 Données Filtrées")
st.dataframe(filtered_df)

# Option pour télécharger les données filtrées
st.download_button(
    label="📥 Télécharger les données filtrées",
    data=filtered_df.to_csv(index=False).encode("utf-8"),
    file_name="Données_filtrées.csv",
    mime="text/csv"
)
