def homes():
    import streamlit as st
    import numpy as np
    import sklearn
    import sys
    import os
    from cleaning_data import clean_data
    from vectorizer import vectorize
    import tensorflow as tf
    from top5 import top5_func
    
    # Custom navigation function to replace switch_page
    def navigate_to(page_name):
        # Get the current script path
        current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        
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
            
        # Set a flag in session state to navigate after rerun
        st.session_state["navigate_to"] = page_name
        
        # Clear current page and run the target page
        st.rerun()

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

        navigate_to("result")

    else:
        st.write('')
