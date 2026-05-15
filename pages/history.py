import streamlit as st
import pandas as pd
from utils.db import messages_collection

def show_history():

    st.title("🕒 Message History")

    messages = list(

        messages_collection.find(
            {"user": st.session_state.user},
            {"_id": 0}
        )
    )

    if messages:

        df = pd.DataFrame(messages)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No messages found")

    st.markdown("---")
    st.caption("SmartSMS • Developed by Tejni")