import streamlit as st
import pandas as pd

def show_export():
    st.subheader("📤 Export – Ergebnisse speichern")
    st.markdown("Download als CSV (Beispieldaten).")

    data = pd.DataFrame({
        "Fläche": ["A", "B", "C"],
        "Score": [0.85, 0.45, 0.72]
    })

    csv = data.to_csv(index=False).encode('utf-8')

    st.download_button(
        label="📥 CSV herunterladen",
        data=csv,
        file_name="standortanalyse_export.csv",
        mime="text/csv"
    )
