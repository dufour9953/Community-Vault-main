
import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Digital Community Vault", layout="wide")
st.title("🌱 Digital Community Vault")

html_path = Path("index.html")
if html_path.exists():
    components.html(html_path.read_text(), height=700, scrolling=True)
else:
    st.error("Landing page not found.")
