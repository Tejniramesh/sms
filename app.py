import streamlit as st
from streamlit_option_menu import option_menu
from utils.auth import login_user, register_user
from utils.styles import load_css

st.set_page_config(
    page_title="SmartSMS",
    page_icon="📩",
    layout="wide"
)

load_css()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("📩 SmartSMS")
    st.subheader("Modern SMS Management System")

    auth_option = st.radio(
        "Choose Option",
        ["Login", "Register"],
        horizontal=True
    )

    if auth_option == "Login":

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Login"):

            with st.spinner("Logging in..."):

                success = login_user(email, password)

                if success:
                    st.session_state.logged_in = True
                    st.session_state.user = email
                    st.success("Login successful")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    else:

        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Register"):

            success = register_user(username, email, password)

            if success:
                st.success("Registration successful")
            else:
                st.error("User already exists")

else:

    selected = option_menu(
        menu_title="SmartSMS",
        options=[
            "Dashboard",
            "Send SMS",
            "Contacts",
            "History",
            "Analytics",
            "Logout"
        ],
        icons=[
            "house",
            "chat-dots",
            "people",
            "clock-history",
            "bar-chart",
            "box-arrow-right"
        ],
        menu_icon="chat",
        default_index=0,
        orientation="horizontal"
    )

    if selected == "Dashboard":
        from pages.dashboard import show_dashboard
        show_dashboard()

    elif selected == "Send SMS":
        from pages.send_sms import show_send_sms
        show_send_sms()

    elif selected == "Contacts":
        from pages.contacts import show_contacts
        show_contacts()

    elif selected == "History":
        from pages.history import show_history
        show_history()

    elif selected == "Analytics":
        from pages.analytics import show_analytics
        show_analytics()

    elif selected == "Logout":
        st.session_state.logged_in = False
        st.rerun()
