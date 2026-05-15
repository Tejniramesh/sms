import streamlit as st
from streamlit_option_menu import option_menu
from utils.auth import login_user, register_user
from utils.styles import load_css

# Page configuration
st.set_page_config(
    page_title="SmartSMS",
    page_icon="📩",
    layout="wide"
)

# Load custom CSS
load_css()

# Session setup
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LANDING PAGE ---------------- #

if not st.session_state.logged_in:

    st.markdown("""
    # 📩 SmartSMS

    ### Modern SMS Management System

    Send messages, manage contacts, track analytics — all in one dashboard.
    """)

    st.markdown("---")

    auth_option = st.radio(
        "Choose Option",
        ["Login", "Register"],
        horizontal=True
    )

    # ---------------- LOGIN ---------------- #

    if auth_option == "Login":

        st.subheader("🔐 Login")

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

    # ---------------- REGISTER ---------------- #

    else:

        st.subheader("📝 Register")

        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Create Account"):

            with st.spinner("Creating account..."):

                success = register_user(
                    username,
                    email,
                    password
                )

                if success:
                    st.success("Account created successfully")

                else:
                    st.error("User already exists")

# ---------------- MAIN APP ---------------- #

else:

    with st.sidebar:

        st.image(
            "assets/logo.png",
            width=120
        )

        st.markdown("## 📩 SmartSMS")

        selected = option_menu(
            menu_title=None,
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
            default_index=0
        )

        st.markdown("---")
        st.caption("Developed by Tejni")

    # Page routing

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