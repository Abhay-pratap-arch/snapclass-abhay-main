import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
                .stApp {
                    background: #5865F2 !important;
                }

                .stApp div[data-testid="stColumn"] {
                    background-color: #E0E3FF !important;
                    padding: 2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>
        """,unsafe_allow_html=True)

def style_background_dashboard():
    st.markdown(
        """
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def style_background_layout():
    st.markdown(
        """
        <style>
            /* Import Google Fonts */
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&family=Outfit:wght@100..900&display=swap');

            # /* Hide top toolbar, footer, and header */
            # #MainMenu, footer, header {
            #     visibility: hidden;
            # }

            .block-container {
                padding-top:5rem !important;
            }

            h1, h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 2.5rem !important;
                line-height:2.52rem !important;
                margin-bottom:0% !important; 
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;
            }

            button {
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                transform: scale(1.05);
            }
        </style>
        """,
        unsafe_allow_html=True
    )
