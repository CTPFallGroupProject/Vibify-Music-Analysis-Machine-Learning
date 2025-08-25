
import streamlit as st
import sys
import os

# Custom navigation function to replace switch_page
def navigate_to(page_name):
    # Get the current script path
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Construct the path to the target page
    if page_name == "app":
        target_path = os.path.join(current_dir, "app.py")
    elif page_name == "result":
        target_path = os.path.join(current_dir, "pages", "result.py")
    else:
        st.error(f"Unknown page: {page_name}")
        return
    
    # Check if the file exists
    if not os.path.isfile(target_path):
        st.error(f"Page not found: {target_path}")
        return
        
    # Set a flag in session state to navigate after rerun
    st.session_state["navigate_to"] = page_name
    
    # Clear current page and run the target page
    st.rerun()
st.set_page_config(
    page_title="Vibify - About Us",
    page_icon="🎵",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Only hide the main menu and footer, not the header (which contains sidebar controls)
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
div.block-container {padding-top: 1rem;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Using default Streamlit navigation



def set_bg_hack_url():
    '''
    A function to set the background.
    Returns
    -------
    The background.
    '''
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url("https://cdn.pixabay.com/photo/2015/12/27/05/48/turntable-1109588_1280.jpg");
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
    # Use local image path
    st.image("streamlit-app/images/Aleks.png")

    st.markdown(
        "<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'><h5 style='text-align: center; color: black;'>Aleksandra Georgievska</h5>", unsafe_allow_html=True)

    st.markdown("<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'>Aleksandra is Senior studying CS at Queens College and a Data Science Fellow with CUNY Tech Prep. She is passionate about Data/ML/AI and is building on 10+ years of professional experience in the music industry and financial compliance. Expected grad Dec '23.</div>", unsafe_allow_html=True)

    st.markdown("<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'><a href='https://www.linkedin.com/in/aleksgeorgi/'> find me on LinkedIn</a><br><a href='https://github.com/aleksgeorgi'> find me on Github</a></div>", unsafe_allow_html=True)

with col2:
    # Use local image path
    st.image("streamlit-app/images/Deep.png")

    st.markdown(
        "<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'><h5 style='text-align: center; color: black;'>Deepankar Ckakraborty</h5>", unsafe_allow_html=True)

    st.markdown("<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'>Deepankar is a Junior at CCNY, studying CS. Has a passion for applying data driven solution to problems. Want to apply Machine Learning knowledge to build something cool.</div>", unsafe_allow_html=True)

    st.markdown("<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'><a href='https://www.linkedin.com/in/deepankar-ckakraborty-327691101/'> find me on LinkedIn</a><br><a href='https://github.com/deepankarck2'> find me on Github</a></div>", unsafe_allow_html=True)

with col3:
    # Use local image path
    st.image("streamlit-app/images/Stephen.png")
    st.markdown(
        "<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'><h5 style='text-align: center; color: black;'>Stephen Williams</h5>", unsafe_allow_html=True)
    st.markdown("<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'>Stephen is a senior at John Jay College studying Applied Math and Computer Science. Loves building NLP models and hopes to pursue a career in data science</div>", unsafe_allow_html=True)

    st.markdown("<div style='background-color: white; padding: 10px; border-radius: 5px; opacity: 0.9;'><a href='https://www.linkedin.com/in/stephen-williams-7843271a3/'> find me on LinkedIn</a><br><a href='https://github.com/Svalentinow'> find me on Github</a></div>", unsafe_allow_html=True)

