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
    elif page_name == "about_us":
        target_path = os.path.join(current_dir, "pages", "about_us.py")
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
    page_title="Vibify - Results",
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
    A function to unpack an image from url and set as bg.
    Returns
    -------
    The background.
    '''
    st.markdown(
        f"""
            <style>
            .stApp {{
                background: url("https://i.imgur.com/akdsDra.jpg");
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
        .css-1n76uvr{{
            color: black !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


set_bg_hack_url()
set_prompt_input_color()

dict = {
    '0': 'Country',
    '1': "Pop",
    '2': "R&B",
    '3': 'Rap',
    '4': 'Rock',

}

# Check if we have prediction results in session state
if 'prediction_valence' in st.session_state and 'prediction_genre' in st.session_state and 'top5_list' in st.session_state:
    st.write("Positive/Negative Sentiment Prediction: ", st.session_state['prediction_valence'])
    st.write("a rating of 0 = very sad, 1 = very happy")
    st.write(" ")
    st.write("Genre Prediction is: ", dict.get(str(st.session_state['prediction_genre'])))
    
    # Check if top5_list exists and has items
    if st.session_state.top5_list and len(st.session_state.top5_list) > 0:
        st.write("Top 5 Lyrically Similar Songs Are: \n")
        for i, song in enumerate(st.session_state.top5_list[:5]):
            st.write(f"{i+1}) {song}")
    else:
        st.write("No similar songs found.")
else:
    st.error("No prediction results found. Please go to the Predict page and submit lyrics first.")