import streamlit as st

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
    **LinkedIn:** [linkedin.com/in/shaikhsadique](https://linkedin.com/in/shaikhsadique)  
    """
)