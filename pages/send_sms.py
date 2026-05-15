import streamlit as st
from utils.sms import send_sms

def show_send_sms():

    st.title("📩 Send SMS")

    phone = st.text_input("Phone Number")
    message = st.text_area("Message")

    if st.button("Send Message"):

        if phone and message:

            with st.spinner("Sending SMS..."):

                send_sms(
                    st.session_state.user,
                    phone,
                    message
                )

                st.success("SMS Sent Successfully")

        else:
            st.error("Please fill all fields")
