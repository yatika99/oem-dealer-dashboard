# dealer_dashboard.py - Plotly-Free Version
import streamlit as st
import pandas as pd
import numpy as np

# Streamlit page settings
st.set_page_config(page_title="OEM Dealer Dashboard", layout="wide")

# Title
st.title("🚗 OEM Dealer Performance Management System")
st.subheader("📌 Dealer Overview")

# Dealer Info Section
dealer_info = {
    "Dealer Code": "DLR-001",
    "Dealer Type": "3S (Sales, Service, Spares)",
    "Region": "North",
    "Evaluation Score": 87,
    "Way Forward": "Greenfield",
    "Category": "PIP"
}

cols = st.columns(6)
for i, (k, v) in enumerate(dealer_info.items()):
    cols[i].metric(label=k, value=str(v))

# Tabs for different sections
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Sales", "🛠️ Service", "🏢 CI/SI", "🎓 Training", "⚠️ Deviations"])

# Sales Tab
with tab1:
    st.subheader("Sales KPIs")
    col1, col2, col3 = st.columns(3)
    col1.number_input("Sales (Units)", value=150)
    col2.number_input("Sales Value (₹ Lakhs)", value=120)
    col3.text_input("Retail vs Wholesale Ratio", "1.2")

    col4, col5, col6 = st.columns(3)
    col4.number_input("Fund Gap (₹)", value=500000)
    col5.slider("Market Share (%)", 0, 100, 18)
    col6.selectbox("Market Share Trend", ["Growing", "Declining", "Stagnant"])

    sales_data = pd.DataFrame({
        "Quarter": ["Q1", "Q2", "Q3", "Q4"],
        "Retail": [120, 150, 130, 160],
        "Wholesale": [100, 120, 115, 130]
    })
    
    # Using native Streamlit bar chart
    st.bar_chart(sales_data.set_index("Quarter"), 
                 color=["#FF0000", "#0000FF"])

# Service Tab
with tab2:
    st.subheader("Service KPIs")
    st.number_input("Service Load (vehicles/month)", value=450)
    st.slider("Repeat Jobs (%)", 0, 100, 8)
    st.slider("Parts Availability (%)", 0, 100, 92)
    st.slider("Customer Satisfaction Index (CSI)", 0, 100, 85)

# CI/SI Tab
with tab3:
    st.subheader("CI & SI Compliance")
    st.selectbox("Digital Board Status", ["Installed", "Pending", "Not Applicable"])
    st.selectbox("Facia Installation", ["Complete", "Partial", "Not Started"])
    st.selectbox("Seating Area Setup", ["Done", "Pending"])
    st.selectbox("Information Boards", ["Available", "Missing"])

# Training Tab
with tab4:
    st.subheader("Training Tracker")
    st.multiselect("Completed Trainings", ["Sales Excellence", "Service Protocol", "DMS Training"])
    st.multiselect("Ongoing Trainings", ["Electric Vehicle Workshop", "CRM Tool Training"])
    st.multiselect("Planned Trainings", ["CI Compliance", "Dealer Audit Prep"])

# Deviations Tab
with tab5:
    st.subheader("Deviation Monitoring")
    st.text_area("Stock Variance", "2.5% below target")
    st.text_area("Target vs Actual Sales", "15% below Q2 target")
    st.text_area("Service Backlogs", "27 pending cases >7 days")
    st.text_area("Unresolved Complaints", "3 escalated to OEM")

st.markdown("---")
st.caption("© 2025 OEM Dealer Analytics | Internal Use Only")
