import streamlit as st
import datetime

def apply_custom_styles():
    """Inject custom CSS for a modern SaaS-style look."""
    custom_css = """
    <style>
    /* --- General --- */
    html, body, [class*="st-"], .css-18e3th9 {
        font-family: 'Inter', sans-serif;
    }
    /* Full-page gradient background */
    .stApp {
        background: #FFFFFF;
    }
    /* --- Main area card look --- */
    .main > div {
        background: #ffffff;
        border-top-left-radius: 16px;
        border-top-right-radius: 16px;
        padding: 2rem 2rem 4rem 2rem;
        min-height: 100vh;
    }
    /* --- Sidebar --- */
    section[data-testid=\"stSidebar\"] > div:first-child {
        background-color: #FFFFFF;
        padding: 1.5rem 1rem;
        box-shadow: 2px 0 6px rgba(0,0,0,0.05);
    }
    section[data-testid=\"stSidebar\"] label, section[data-testid=\"stSidebar\"] p {
        color: #000000;
    }
    /* Sidebar header */
    .sidebar-logo {
        font-size: 1.4rem;
        font-weight: 700;
        color: #5B6EF5;
        margin-bottom: 2rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    /* Metric card */
    .metric-card {
        background: #ffffff;
        padding: 1rem;
        border-radius: 0.7rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        margin-top: 0.2rem;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #6c6c6c;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)


def top_bar():
    """Render a top navigation bar with greeting and settings icon."""
    with st.container():
        col1, col2 = st.columns([6,1])
        with col1:
            st.markdown("## 👋 Welcome! Today is **{}**".format(datetime.date.today().strftime('%B %d, %Y')))
        with col2:
            st.markdown("<div style='text-align:right;font-size:24px'>⚙️</div>", unsafe_allow_html=True)