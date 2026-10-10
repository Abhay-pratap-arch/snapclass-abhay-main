import streamlit as st 

def footer_home():
    logo_url = "https://i.postimg.cc/ydBM0Q6X/Copilot-20261010-114541.png"
    st.markdown(f""" 
            <div style="margin-top:2rem; display:flex; gap:6px;justify-content:center; items-align:center"> 
            <p style=color:white;font-weight:bold;> Created with❤️by</p>
            <img src='{logo_url}' style='max-height:95px'px/>
            </div>
               """,unsafe_allow_html=True)

def footer_dashboard():
    logo_url = "https://i.postimg.cc/ydBM0Q6X/Copilot-20261010-114541.png"
    st.markdown(f""" 
            <div style="margin-top:2rem; display:flex; gap:6px;justify-content:center; items-align:center"> 
            <p style=color:black;font-weight:bold;> Created with❤️by</p>
            <img src='{logo_url}' style='max-height:95px'px/>
            </div>
               """,unsafe_allow_html=True)