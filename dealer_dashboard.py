# dealer_dashboard.py - Enhanced Visual Version
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# Page Config
st.set_page_config(page_title="OEM Dealer Dashboard Pro", layout="wide", page_icon="🚗")

# Custom CSS
st.markdown("""
<style>
    .header-style { font-size:24px !important; font-weight:bold !important; color:#2a3f5f }
    .metric-card { 
        background: white; border-radius:10px; padding:15px 20px; 
        box-shadow:0 4px 6px rgba(0,0,0,0.1); margin-bottom:15px 
    }
    .progress-bar {
        height:10px; background:#e0e0e0; border-radius:5px; margin-top:5px
    }
    .progress-fill {
        height:100%; border-radius:5px; background:#4CAF50
    }
</style>
""", unsafe_allow_html=True)

# Current Date
current_date = datetime.now().strftime("%d %b %Y")

# --- Header ---
st.title(f"🚗 OEM Dealer Performance Dashboard")
st.markdown(f"*Last Updated: {current_date}*")

# --- Dealer Summary Cards ---
cols = st.columns(4)
with cols[0]:
    st.markdown('<div class="metric-card"><div class="header-style">DLR-001</div>North Region</div>', unsafe_allow_html=True)
with cols[1]:
    st.markdown('<div class="metric-card"><div class="header-style">87/100</div>Evaluation Score</div>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<div class="metric-card"><div class="header-style">3S</div>Sales | Service | Spares</div>', unsafe_allow_html=True)
with cols[3]:
    st.markdown('<div class="metric-card"><div class="header-style">PIP</div>Performance Category</div>', unsafe_allow_html=True)

# --- Main Tabs ---
tab1, tab2, tab3, tab4, tab5 = st.tabs(["📈 Sales Performance", "📊 Market Analytics", "👥 Manpower", "📱 Digital Metrics", "⚠️ Issues Tracking"])

# ===== SALES PERFORMANCE TAB =====
with tab1:
    st.markdown('<div class="header-style">Sales Performance Dashboard</div>', unsafe_allow_html=True)
    
    # Row 1: Institutional vs Retail Performance
    st.subheader("Institutional vs Retail Performance")
    col1, col2 = st.columns([2,1])
    
    with col1:
        # Combo Chart Data
        sales_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Retail Target': [120, 130, 125, 140, 150, 160],
            'Retail Actual': [115, 125, 130, 135, 145, 155],
            'Institutional Target': [80, 85, 90, 95, 100, 105],
            'Institutional Actual': [75, 80, 85, 90, 95, 100],
            'Achievement %': [92, 94, 102, 96, 97, 97]
        })
        
        # Create combo chart using native Streamlit
        st.write("**Retail Performance**")
        st.bar_chart(sales_data, x='Month', y=['Retail Target', 'Retail Actual'])
        st.write("**Institutional Performance**")
        st.bar_chart(sales_data, x='Month', y=['Institutional Target', 'Institutional Actual'])
        st.write("**Achievement Percentage Trend**")
        st.line_chart(sales_data, x='Month', y='Achievement %')
    
    with col2:
        st.write("**Current Month Summary**")
        st.metric("Retail Achievement", "155/160", "97%")
        st.metric("Institutional Achievement", "100/105", "95%")
        st.progress(96, text="Overall Achievement")
        
        st.write("**Quarterly Trend**")
        quarterly = pd.DataFrame({
            'Quarter': ['Q1', 'Q2'],
            'Growth %': [8.5, 7.2]
        })
        st.bar_chart(quarterly, x='Quarter', y='Growth %')

# ===== MARKET ANALYTICS TAB =====
with tab2:
    st.markdown('<div class="header-style">Market Analytics Dashboard</div>', unsafe_allow_html=True)
    
    # Company Snapshot
    st.subheader("Company Snapshot")
    cols = st.columns(4)
    with cols[0]:
        st.metric("Volume", "12,450", "8.5% vs LY")
    with cols[1]:
        st.metric("Market Share", "18.2%", "0.7pp vs LY")
    with cols[2]:
        st.metric("Retail Mix", "62%", "4% vs LY")
    with cols[3]:
        st.metric("Inventory Days", "28", "-3 vs LY")
    
    # Competitor Analysis
    st.subheader("Competitor Benchmarking")
    comp_data = pd.DataFrame({
        'Brand': ['OEM', 'Competitor A', 'Competitor B', 'Competitor C'],
        'Volume': [12450, 15200, 9800, 8700],
        'Growth LY': [8.5, 5.2, 12.1, -2.4],
        'MS Change': [0.7, -0.3, 1.1, -1.5]
    })
    st.dataframe(comp_data.style
                .background_gradient(subset=['Growth LY'], cmap='RdYlGn')
    
    # Market Share Trend
    st.subheader("Market Share Trend (Last 6 Months)")
    ms_data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'OEM': [17.5, 17.8, 18.0, 18.1, 18.2, 18.2],
        'Comp A': [22.1, 21.8, 21.5, 21.3, 21.1, 20.9],
        'Comp B': [14.5, 14.8, 15.1, 15.3, 15.5, 15.6]
    })
    st.line_chart(ms_data.set_index('Month'))

# ===== MANPOWER TAB =====
with tab3:
    st.markdown('<div class="header-style">Manpower Dashboard</div>', unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        st.subheader("Staffing Levels")
        staffing = pd.DataFrame({
            'Role': ['Sales', 'Service', 'Support', 'Management'],
            'Current': [8, 12, 5, 3],
            'Required': [10, 15, 6, 3],
            'Vacancy %': [20, 20, 17, 0]
        })
        st.dataframe(staffing.style
                    .bar(subset=['Vacancy %'], align='left', color=['#ff6961']))
    
    with cols[1]:
        st.subheader("Training Completion")
        training = pd.DataFrame({
            'Program': ['Sales Excellence', 'Service Protocol', 'DMS Training', 'EV Workshop'],
            'Completion %': [85, 92, 78, 45]
        })
        st.bar_chart(training, x='Program', y='Completion %')

# ===== DIGITAL METRICS TAB =====
with tab4:
    st.markdown('<div class="header-style">Digital Engagement Dashboard</div>', unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        st.subheader("App Enrollment")
        app_data = pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'Enrollment %': [35, 42, 48, 53, 58, 62]
        })
        st.area_chart(app_data, x='Month', y='Enrollment %')
        st.metric("Current Enrollment", "62%", "4% MoM growth")
    
    with cols[1]:
        st.subheader("Service Quality Index")
        sqi_data = pd.DataFrame({
            'Parameter': ['Timeliness', 'Quality', 'Communication', 'Facility'],
            'Score': [82, 88, 79, 85]
        })
        st.bar_chart(sqi_data, x='Parameter', y='Score')

# ===== ISSUES TRACKING TAB =====
with tab5:
    st.markdown('<div class="header-style">Issues & Complaints Dashboard</div>', unsafe_allow_html=True)
    
    cols = st.columns(2)
    with cols[0]:
        st.subheader("Customer Complaints")
        complaints = pd.DataFrame({
            'Type': ['Service Delay', 'Parts Availability', 'Billing', 'Quality'],
            'Count': [15, 22, 8, 5],
            'Resolution %': [80, 65, 100, 100]
        })
        st.bar_chart(complaints, x='Type', y='Count')
    
    with cols[1]:
        st.subheader("Deviation Tracking")
        deviations = {
            'Stock Variance': '2.5% below target',
            'Sales Target': '15% below Q2 target',
            'Service Backlogs': '27 pending cases >7 days',
            'Unresolved Complaints': '3 escalated to OEM'
        }
        for k, v in deviations.items():
            with st.expander(k):
                st.write(v)
                st.progress(75)

# Footer
st.markdown("---")
st.markdown("**© 2025 OEM Dealer Analytics Pro** | *Internal Use Only* | v2.0")
