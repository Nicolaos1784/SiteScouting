import streamlit as st

st.title("🚀 SiteScouting – Standortanalyse für Gewerbeflächen")

from pages.map_view import show_map
from pages.ranking_view import show_ranking
from pages.export_view import show_export

# Konfiguration der Streamlit-Web-App
st.set_page_config(
    page_title="Gewerbeflächenanalyse Frankfurt",
    layout="wide"
)

# Titelbild und Kopfzeile
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/75/Frankfurt_Skyline_Panorama.jpg",
    use_container_width=True
)

st.title("📍 Standortanalyse Gewerbeflächen – Großraum Frankfurt")

st.markdown("""
Willkommen zur digitalen Standortanalyse Großraum Frankfurt.  
Diese Anwendung unterstützt Sie bei der Identifikation, Bewertung und Auswahl optimaler Gewerbeflächen für Rechenzentren, Logistik oder Life Sciences.

Nutzen Sie die Navigationsleiste links, um Karten zu analysieren, Flächen zu bewerten oder Daten zu exportieren.
""")

# Navigationsmenü in der Seitenleiste
menu = st.sidebar.radio("📂 Navigation", [
    "🌍 Karte",
    "📊 Ranking",
    "📤 Export"
])

# Seiteninhalt basierend auf Navigation
if menu == "🌍 Karte":
    show_map()
elif menu == "📊 Ranking":
    show_ranking()
elif menu == "📤 Export":
    show_export()

