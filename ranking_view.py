import streamlit as st
import pandas as pd

def show_ranking():
    st.subheader("📊 Ranking – Bewertung nach Kriterien")
    st.markdown("Bewertung der Flächen nach Score (Dummy-Daten).")

    # Dummy-Daten
    data = pd.DataFrame({
        "Fläche": ["A", "B", "C"],
        "Entfernung Umspannwerk (m)": [1200, 3500, 980],
        "Hangneigung (%)": [3, 12, 6],
        "Score": [0.85, 0.45, 0.72]
    }).sort_values(by="Score", ascending=False)

    st.dataframe(data, use_container_width=True)
