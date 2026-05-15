import streamlit as st
import pandas as pd
from utils.db import contacts_collection

def show_contacts():

    st.title("👥 Contacts")

    name = st.text_input("Contact Name")
    phone = st.text_input("Phone Number")

    if st.button("Add Contact"):

        contacts_collection.insert_one({
            "name": name,
            "phone": phone
        })

        st.success("Contact Added")

    contacts = list(contacts_collection.find({}, {"_id": 0}))

    if contacts:

        df = pd.DataFrame(contacts)
        st.dataframe(df, use_container_width=True)
