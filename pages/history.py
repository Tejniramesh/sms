import streamlit as st
import pandas as pd
from utils.db import messages_collection

def show_history():

    st.title("🕒 Message History")

    messages = list(
        messages_collection.find({}, {"_id": 0})
    )

    if messages:

        df = pd.DataFrame(messages)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.info("No messages found")
