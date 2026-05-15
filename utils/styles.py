import streamlit as st

def load_css():

    st.markdown(
        '''
        <style>
        .stApp {
            background-color: #0f172a;
            color: white;
        }

        .stButton button {
            width: 100%;
            border-radius: 10px;
            height: 45px;
            font-size: 16px;
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
