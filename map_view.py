import streamlit as st
import folium
from streamlit_folium import folium_static

def show_map():
    st.subheader("🌍 Kartenansicht – Infrastruktur & Kriterien")
    st.markdown("Zeigt interaktive Karte mit beispielhaften Markern für Umspannwerke und Gewerbeflächen.")

    # Karte initialisieren
    m = folium.Map(location=[50.1109, 8.6821], zoom_start=11)

    # Beispielhafte Marker
    folium.Marker(
        location=[50.11, 8.68],
        popup="Musterfläche A",
        icon=folium.Icon(color="green")
    ).add_to(m)

    folium.Marker(
        location=[50.12, 8.70],
        popup="Umspannwerk Süd",
        icon=folium.Icon(color="red")
    ).add_to(m)

    folium_static(m, width=1000, height=600)
