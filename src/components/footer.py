import streamlit as st 

def footer_home():
    logo_url = "https://copilot.microsoft.com/th/id/BCO.0dbd8005-290c-47e8-acc0-2c4013117de5.png"
    st.markdown(f""" 
            <div style="margin-top:2rem; display:flex; gap:6px;justify-content:center; items-align:center"> 
            <p style=color:white;font-weight:bold;> Created with❤️by</p>
            <img src='{logo_url}' style='max-height:75px'px/>
            </div>
               """,unsafe_allow_html=True)

def footer_dashboard():
    logo_url = "https://copilot.microsoft.com/th/id/BCO.0dbd8005-290c-47e8-acc0-2c4013117de5.png"
    st.markdown(f""" 
            <div style="margin-top:2rem; display:flex; gap:6px;justify-content:center; items-align:center"> 
            <p style=color:black;font-weight:bold;> Created with❤️by</p>
            <img src='{logo_url}' style='max-height:75px'px/>
            </div>
               """,unsafe_allow_html=True)