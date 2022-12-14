
from streamlit.runtime.scriptrunner.script_run_context import get_script_run_ctx
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(initial_sidebar_state="collapsed")


selected = option_menu(None, ["Predict", "About Us"],
                       icons=['cloud-upload', "bi-file-person"],
                       menu_icon="cast",
                       default_index=1,
                       orientation="horizontal",
                       styles={
    "container": {"padding": "1!important", "background-color": "#fafafa"}, })


def set_bg_hack_url():
    '''
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://i.imgur.com/KVwLF3p.jpg");
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def set_prompt_input_color():
    st.markdown(
        f"""
        <style>
        .css-184tjsw.e16nr0p34 > p {{
            color: white !important;
            font-weight: 900;
            font-size: 23px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_bg_hack_url()
set_prompt_input_color()

col1, col2, col3 = st.columns([1, 1, 1])

with col1:

    url1 = 'https://drive.google.com/file/d/1vu9PCDvJtRWeYmZ3SfDH_QN8oiufLlcd/view?usp=sharing'
    url1 = 'https://drive.google.com/uc?id=' + url1.split('/')[-2]
    st.image(url1)

    st.markdown(
        "<h5 style='text-align: center; color: black;'>Aleksandra Georgievska</h5>", unsafe_allow_html=True)

    st.write("Aleksandra is Senior studying CS at Queens College and a Data Science Fellow with CUNY Tech Prep. She is passionate about Data/ML/AI and is building on 10+ years of professional experience in the music industry and financial compliance. Expected grad Dec '23.")

    st.write('<a href="https://www.linkedin.com/in/aleksgeorgi/"> find me on LinkedIn</a>',
             unsafe_allow_html=True)
    st.write('<a href="https://github.com/aleksgeorgi"> find me on Github</a>',
             unsafe_allow_html=True)

with col2:

    url2 = 'https://drive.google.com/file/d/1sShRuqdlErHOVIXxqgtS6JIST4oQZOuB/view?usp=sharing'
    url2 = 'https://drive.google.com/uc?id=' + url2.split('/')[-2]
    st.image(url2)

    st.markdown(
        "<h5 style='text-align: center; color: black;'>Deepankar Ckakraborty</h5>", unsafe_allow_html=True)

    st.write("Deepankar is a Junior at CCNY, studying CS. Has a passion for applying data driven solution to problems. Want to apply Machine Learning knowledge to build something cool.")

    st.write('<a href="https://www.linkedin.com/in/deepankar-ckakraborty-327691101/"> find me on LinkedIn</a>',
             unsafe_allow_html=True)
    st.write('<a href="https://github.com/deepankarck2"> find me on Github</a>',
             unsafe_allow_html=True)

with col3:
    url3 = 'https://drive.google.com/file/d/1LAmVoquj-Gks1eJlcFnXQFIN5gh0gR8M/view?usp=sharing'
    url3 = 'https://drive.google.com/uc?id=' + url3.split('/')[-2]
    st.image(url3)
    st.markdown(
        "<h5 style='text-align: center; color: black;'>Stephen Williams</h5>", unsafe_allow_html=True)
    st.write("Stephen is a senior at John Jay College studying Applied Math and Computer Science. Enjoys learning the capabilities of AI and hopes to pursue a career in data science")

    st.write('<a href="https://www.linkedin.com/in/stephen-williams-7843271a3/"> find me on LinkedIn</a>',
             unsafe_allow_html=True)
    st.write('<a href="https://github.com/Svalentinow"> find me on Github</a>',
             unsafe_allow_html=True)

    if selected == "Predict":
        switch_page("app")
