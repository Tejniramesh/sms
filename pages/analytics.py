import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from utils.db import messages_collection

def show_analytics():

    st.title("📈 Analytics")

    messages = list(
        messages_collection.find({}, {"_id": 0})
    )

    if not messages:
        st.warning("No data available")
        return

    df = pd.DataFrame(messages)

    status_counts = df["status"].value_counts()

    fig, ax = plt.subplots()

    ax.bar(
        status_counts.index,
        status_counts.values
    )

    ax.set_title("SMS Status Overview")

    st.pyplot(fig)
