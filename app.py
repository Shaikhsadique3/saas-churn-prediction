import streamlit as st
from ui_helper import apply_custom_styles, top_bar

st.set_page_config(
    page_title="Churn Prediction App",
    page_icon=":bar_chart:",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🧠 Welcome to Churnaizer")
st.write("Your all-in-one churn prediction and retention analytics system for SaaS businesses.")
st.write("This dashboard turns customer data into actionable insights — helping founders reduce churn, improve retention, and protect recurring revenue.")


st.sidebar.success("Select a page above.")

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

st.markdown(
    """
    This dashboard helps you predict customer churn and gain valuable insights.

    

    ### What's inside?
    - **Insights:** Explore key churn metrics, trends, and performance indicators.
    - **Recommendations:** Discover actionable retention strategies based on churn segments.
    - **Predict:** Upload your own data to simulate churn risk and revenue impact.

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
    **X (Twitter):** [x.com/Shaikh_Sadique3](https://x.com/Shaikh_Sadique3)  
    **LinkedIn:** [linkedin.com/in/shaikh-sadique-131341356](https://www.linkedin.com/in/shaikh-sadique-131341356)  
    """
)

st.subheader("Graphs Explained")
with st.expander("See details of each visualization"):
    # --- 1. Churn Probability by Plan Type ---
    st.markdown("### 1. Churn Probability by Plan Type")
    st.image("images/churn_by_plan.png", use_container_width=True)
    st.markdown(
        """
**X-Axis:** Plan type (Free, Basic, Pro …)  
**Y-Axis:** Churn probability (%)  
**What It Shows:** Compares churn likelihood across different subscription tiers.  
**Business Benefit:** Highlights which plans need retention initiatives or pricing tweaks.
        """
    )

    # --- 2. Feature Adoption vs Churn Risk ---
    st.markdown("### 2. Feature Adoption vs Churn Risk")
    st.image("images/churn_by_features.png", use_container_width=True)
    st.markdown(
        """
**X-Axis:** Number of active features used  
**Y-Axis:** Churn probability (%)  
**What It Shows:** Relationship between product engagement (feature usage) and churn.  
**Business Benefit:** Reveals under-used features and upsell or education opportunities.
        """
    )

    # --- 3. Cohort Retention by Signup Month ---
    st.markdown("### 3. Cohort Retention by Signup Month")
    st.image("images/cohort_retention.png", use_container_width=True)
    st.markdown(
        """
**X-Axis:** Signup month  
**Y-Axis:** Retention (%)  
**What It Shows:** Retention trend over time for user cohorts.  
**Business Benefit:** Detects seasonal issues and measures impact of experiments or campaigns.
        """
    )

    # --- 4. Top 10 Churn Drivers (SHAP) ---
    st.markdown("### 4. Top 10 Churn Drivers (SHAP)")
    st.image("images/top_shap_drivers.png", use_container_width=True)
    st.markdown(
        """
**X-Axis:** Features (ranked by importance)  
**Y-Axis:** Importance score (mean |SHAP|)  
**What It Shows:** Variables that most influence the churn model’s predictions.  
**Business Benefit:** Focuses roadmap and marketing efforts on high-impact factors.
        """
    )