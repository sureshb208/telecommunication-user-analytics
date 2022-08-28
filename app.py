import streamlit as st
from PIL import Image
from graphs import overview_app


st.set_page_config(page_title="Telcom Data Analysis")


styles = {
    "container": {"padding": "0!important", "background-color": "#fafafa"},
    "icon": {"color": "orange", "font-size": "25px"},
    "nav-link": {"font-size": "25px", "text-align": "left", "margin": "0px", "--hover-color": "#eee"},
    "nav-link-selected": {"background-color": "green"},
}
st.title("Telecom Data Analysis")


overview_app()