import streamlit as st
from utils.css_loader import load_css
from streamlit_option_menu import option_menu
from tabs.general_results import general_results
from tabs.team_results import team_results
from tabs.about_me import about_me

load_css()

# Menu de navegação
with st.sidebar:
    selected = option_menu(
        menu_title="",  
        options=["Home", "General Results", "Team Results", "About Me"],
        icons=["house", "bar-chart", "person", "info-circle"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#3c1c5c"},
            "icon": {"color": "white", "font-size": "20px"},
            "nav-link": {
                "font-size": "16px",
                "text-align": "left",
                "margin": "5px",
                "color": "white",
                "background-color": "transparent"
            },
            "nav-link-selected": {
                "background-color": "#3d7499",
                "color": "white"
            },
        }
    )

# Conteúdo baseado na aba selecionada
if selected == "Home":
    st.markdown(f"<img src='./app/static/img/pl.png' width='700'>", unsafe_allow_html=True)
    st.markdown("<h1 class='fancy-title'>Statistics</h1>", unsafe_allow_html=True)
elif selected == "General Results":
    general_results()
elif selected == "Team Results":
    team_results()
elif selected == "About Me":
    about_me()
