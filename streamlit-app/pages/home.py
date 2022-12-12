def homes():
    import streamlit as st
    import numpy as np
    from streamlit_option_menu import option_menu
    from cleaning_data import clean_data
    from vectorizer import vectorize
    import pickle
    from tensorflow import keras
    from streamlit_extras.switch_page_button import switch_page
    from top5 import top5_func

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
                background: url("https://i.pinimg.com/originals/a9/1c/bb/a91cbb2170c5f275f17646f919d9a236.jpg");
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

    txt = st.text_area('Please input test:',
                       placeholder="Placeholder", height=140)

    loaded_valence_model = keras.models.load_model('streamlit-app/LSTM_Valence_model.h5')
    loaded_genre_model = keras.models.load_model('streamlit-app/LSTM_Genre_model.h5')

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

        switch_page("result")

    else:
        st.write('Return:')
