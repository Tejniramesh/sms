import streamlit as st

def load_css():

    st.markdown(
        """
        <style>

        .stApp {
            background: linear-gradient(
                to right,
                #0f172a,
                #1e293b
            );
            color: white;
        }

        section[data-testid="stSidebar"] {
            background-color: #111827;
        }

        .stButton button {
            width: 100%;
            border-radius: 12px;
            height: 45px;
            background-color: #2563eb;
            color: white;
            border: none;
            font-weight: bold;
        }

        .stTextInput input,
        .stTextArea textarea {
            border-radius: 10px;
        }

        div[data-testid="metric-container"] {
            background-color: #1e293b;
            border: 1px solid #334155;
            padding: 20px;
            border-radius: 15px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )