import streamlit as st
from utils.db import contacts_collection, messages_collection

def show_dashboard():

    st.title("📊 Dashboard")

    total_contacts = contacts_collection.count_documents({})
    total_messages = messages_collection.count_documents({})

    col1, col2 = st.columns(2)

    col1.metric("Total Contacts", total_contacts)
    col2.metric("Total Messages", total_messages)

    st.success("Welcome to SmartSMS Dashboard")
