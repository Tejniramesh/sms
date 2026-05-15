import streamlit as st
from utils.db import (
    contacts_collection,
    messages_collection
)

def show_dashboard():

    st.title("📊 Dashboard")

    with st.spinner("Loading dashboard..."):

        total_contacts = contacts_collection.count_documents({
            "user": st.session_state.user
        })

        total_messages = messages_collection.count_documents({
            "user": st.session_state.user
        })

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "👥 Contacts",
        total_contacts
    )

    col2.metric(
        "📩 Messages",
        total_messages
    )

    col3.metric(
        "✅ Status",
        "Active"
    )

    st.markdown("---")

    st.success(
        f"Welcome back, {st.session_state.user}"
    )

    st.markdown("---")
    st.caption("SmartSMS • Developed by Tejni")