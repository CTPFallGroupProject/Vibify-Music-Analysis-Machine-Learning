import streamlit as st
from streamlit_option_menu import option_menu
from pages.home import homes
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(initial_sidebar_state="collapsed")

selected = option_menu(None, ["Predict", "About Us"],
                       icons=['house', 'cloud-upload', "bi-file-person"],
                       menu_icon="cast",
                       default_index=0,
                       orientation="horizontal",
                       styles={
    "container": {"padding": "1!important", "background-color": "#fafafa"}, })

if selected == "Predict":
    homes()

if selected == "About Us":
    switch_page("about_us")


# to run: streamlit run streamlit-app/app.py
