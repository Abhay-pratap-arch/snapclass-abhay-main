import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_background_layout,style_background_home

def home_screen():

    header_home()

    style_background_home()
    style_background_layout()

    # Two-column layout
    col1, col2 = st.columns(2,gap="large")

    
    with col1:
        st.header("I'm Student")
        st.image("https://copilot.microsoft.com/th/id/BCO.be74ae7d-260b-41a0-8b9a-d988da18b421.png",width=120)
        if st.button("Student portal",type="primary",icon=':material/arrow_outward:',icon_position="right"):
            st.session_state['login_type'] ="student"
            st.rerun()

    with col2:
            st.header("I'm Teacher")
            st.image("https://copilot.microsoft.com/th/id/BCO.a4a7fccd-a0c4-4688-a4e9-f4f689196fc4.png",width=120)
            if st.button("Teacher portal",type="primary", icon=':material/arrow_outward:',icon_position="right"):
                st.session_state['login_type'] ="teacher"
                st.rerun()
    footer_home()