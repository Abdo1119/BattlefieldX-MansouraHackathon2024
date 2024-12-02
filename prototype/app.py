import streamlit as st
import streamlit.components.v1 as components

# عنوان التطبيق
st.title("Prototype: Waste Management and Pollution Clustering")
st.markdown("### Select a layer to display:")
st.markdown("- **Locations**: View establishments like restaurants, hospitals, and hotels.")
st.markdown("- **Pollution Clusters**: View pollution clusters with priority levels.")

# قراءة ملف الخريطة HTML
with open("final_map_with_layers.html", "r", encoding="utf-8") as map_file:
    html_content = map_file.read()

# تضمين الخريطة في التطبيق
components.html(html_content, height=800)
