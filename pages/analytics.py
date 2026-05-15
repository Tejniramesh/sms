import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.db import messages_collection

def show_analytics():

    st.title("📈 Analytics")

    messages = list(

        messages_collection.find(
            {"user": st.session_state.user},
            {"_id": 0}
        )
    )

    if not messages:

        st.warning("No analytics data found")
        return

    df = pd.DataFrame(messages)

    df["created_at"] = pd.to_datetime(
        df["created_at"]
    )

    daily_messages = df.groupby(
        df["created_at"].dt.date
    ).size()

    fig, ax = plt.subplots()

    daily_messages.plot(
        kind="line",
        ax=ax
    )

    ax.set_title("Daily SMS Activity")

    st.pyplot(fig)

    st.markdown("---")
    st.caption("SmartSMS • Developed by Tejni")