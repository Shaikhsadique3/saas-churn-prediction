import streamlit as st
from ui_helper import apply_custom_styles, top_bar

st.set_page_config(
    page_title="Churn Prediction App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Welcome to the Churn Prediction Dashboard!")
st.write("Please select a page from the sidebar to get started.")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    This dashboard helps you predict customer churn and gain valuable insights.

    **👈 Select a page from the sidebar** to get started.

    ### What's inside?
    - **Home:** Overview and introduction to the app.
    - **Predict:** Upload your customer data to get churn predictions.
    - **Insights:** Explore visualizations and key performance indicators related to churn.
    - **Business Recommendations:** Get actionable recommendations based on churn risk.

    ---

    ### Churnaizer: A churn prediction and retention analytics system helping SaaS founders identify at-risk customers and automate retention strategy.

    ---

    #### Demo Data Disclaimer
    This dashboard uses demo data for demonstration purposes only. Actual results may vary based on real-world data.
    """
)

st.markdown(
    """
    ---
    **Developed by:** Sadique Shaikh  
    **GitHub:** [github.com/Shaikhsadique3](https://github.com/Shaikhsadique3)  
    **LinkedIn:** [linkedin.com/in/shaikhsadique](https://www.linkedin.com/in/shaikh-sadique-131341356?)  
    """
)

apply_custom_styles()

top_bar()

st.subheader("Key Metrics")
col1,col2,col3,col4=st.columns(4)
with col1:
    st.markdown("<div class='metric-card'>📈<div class='metric-value'>1.2K</div><div class='metric-label'>Total Users</div></div>",unsafe_allow_html=True)
with col2:
    st.markdown("<div class='metric-card'>💰<div class='metric-value'>$42K</div><div class='metric-label'>MRR</div></div>",unsafe_allow_html=True)
with col3:
    st.markdown("<div class='metric-card'>⚠️<div class='metric-value'>5.4%</div><div class='metric-label'>Churn Rate</div></div>",unsafe_allow_html=True)
with col4:
    st.markdown("<div class='metric-card'>⭐<div class='metric-value'>68</div><div class='metric-label'>NPS</div></div>",unsafe_allow_html=True)