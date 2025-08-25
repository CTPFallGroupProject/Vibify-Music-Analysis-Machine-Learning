import streamlit as st
import sys
import os
import numpy as np
import tensorflow as tf
from cleaning_data import clean_data
from vectorizer import vectorize
from top5 import top5_func

# Custom navigation function to replace switch_page
def navigate_to(page_name):
    # Get the current script path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the target page
    if page_name == "about_us":
        target_path = os.path.join(current_dir, "pages", "about_us.py")
    elif page_name == "result":
        target_path = os.path.join(current_dir, "pages", "result.py")
    else:
        st.error(f"Unknown page: {page_name}")
        return
    
    # Check if the file exists
    if not os.path.isfile(target_path):
        st.error(f"Page not found: {target_path}")
        return
        
    # Load the target page as a module
    import importlib.util
    spec = importlib.util.spec_from_file_location(page_name, target_path)
    page_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(page_module)
    
    # Clear current page and run the target page
    st.rerun()
st.set_page_config(
    page_title="Vibify - Home",
    page_icon="🎵",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': "Vibify - A lyrical sentiment analysis app and search engine"
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

# Using the default Streamlit navigation
# No custom navigation needed

# Get the current page from the URL using the non-experimental API
current_page = st.query_params.get("page", "home").lower()

# Only show one page at a time
if current_page == "home":
    # Clear any navigation flags
    if "navigate_to" in st.session_state:
        del st.session_state["navigate_to"]
    
    # Home page content directly in app.py
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
    st.markdown(
        "<h1 style='text-align: center; color: black; background-color: white; opacity: .95'> Welcome to Vibify </1>", unsafe_allow_html=True)

    st.markdown(
        "<h5 style='text-align: center; color: gray; background-color: white; opacity: .95'> Vibify is a Natural Language Processing tool and lyrical search engine helping songwriters, lyricists, and the music-passionate get data on lyrics! </h5>", unsafe_allow_html=True)

    txt = st.text_area('Input Lyrics:',
                       placeholder="...", height=140)

    loaded_valence_model = tf.keras.models.load_model(
        'streamlit-app/LSTM_Valence_model.h5', compile=False)
    loaded_genre_model = tf.keras.models.load_model(
        'streamlit-app/LSTM_Genre_model.h5', compile=False)

    # save variables in the current session
    if "prediction_valence" not in st.session_state:
        st.session_state["prediction_valence"] = ""
        st.session_state["prediction_genre"] = ""
        st.session_state.top5_list = []

    if(st.button('Submit')):
        cleaned_data = clean_data(txt)
        vectorized_data = vectorize(cleaned_data)

        prediction_valence = loaded_valence_model.predict(vectorized_data)
        prediction_genre = np.argmax(
            loaded_genre_model.predict(vectorized_data))

        top5_list = top5_func(cleaned_data)

        st.session_state["prediction_valence"] = prediction_valence
        st.session_state["prediction_genre"] = prediction_genre
        st.session_state["top5_list"] = top5_list

        # Navigate to results page
        st.query_params["page"] = "result"
        st.rerun()
elif current_page == "about_us":
    # Import and run the about_us page directly
    import sys
    import importlib
    
    # Force reload the module to ensure fresh state
    if "pages.about_us" in sys.modules:
        importlib.reload(sys.modules["pages.about_us"])
    
    import pages.about_us
    
# Handle Results page
elif current_page == "result" or current_page == "results":
    # Import and run the result page
    import sys
    import importlib
    
    # Force reload the module to ensure fresh state
    if "pages.result" in sys.modules:
        importlib.reload(sys.modules["pages.result"])
    
    import pages.result
    
# Handle navigation from home page to results
if "navigate_to" in st.session_state and st.session_state["navigate_to"] == "result":
    # Change the URL to the results page using the non-experimental API
    st.query_params["page"] = "result"
    st.rerun()


# to run: streamlit run streamlit-app/app.py
