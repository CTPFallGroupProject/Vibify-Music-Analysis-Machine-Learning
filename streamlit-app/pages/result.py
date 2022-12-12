import streamlit as st
from pages.home import homes
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(initial_sidebar_state="collapsed")


selected = option_menu(None, ["Result", "Predict", "About Us"],
                       icons=['cloud-upload', "bi-file-person"],
                       menu_icon="cast",
                       default_index=0,
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
                background: url("https://c4.wallpaperflare.com/wallpaper/463/870/465/audio-music-earphones-apple-inc-wallpaper-preview.jpg");
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
            color: white !important;
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

st.write("Valence Prediction is: ", st.session_state['prediction_valence'])
st.write("Genre Prediction is: ", dict.get(
    str(st.session_state['prediction_genre'])))
st.write("Top 5 Lyrically Similar Songs Are: \n")
st.write("1) ", st.session_state.top5_list[0])
st.write("2) ", st.session_state.top5_list[1])
st.write("3) ", st.session_state.top5_list[2])
st.write("4) ", st.session_state.top5_list[3])
st.write("5) ", st.session_state.top5_list[4])


if selected == "Predict":
    switch_page("app")

if selected == "About Us":
    switch_page("about_us")
