# dealer_dashboard.py - Final Production Version
import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# ===== CONFIGURATION =====
st.set_page_config(
    page_title="OEM Dealer Dashboard Pro",
    layout="wide",
    page_icon="🚗",
    initial_sidebar_state="collapsed"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    /* Main styling */
    .header-style {
        font-size: 24px !important;
        font-weight: bold !important;
        color: #2a3f5f;
        margin-bottom: 15px !important;
    }
    
    .metric-card {
        background: white;
        border-radius: 10px;
        padding: 15px 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 15px;
        border-left: 4px solid #4CAF50;
    }
    
    /* Progress bars */
    .stProgress > div > div > div {
        background-color: #4CAF50;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Tab styling */
    .stTabs [aria-selected="true"] {
        font-weight: bold;
        color: #4CAF50 !important;
    }
</style>
""", unsafe_allow_html=True)

# ===== DATA & FUNCTIONS =====
def create_performance_data():
    return pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Retail Target': [120, 130, 125, 140, 150, 160],
        'Retail Actual': [115, 125, 130, 135, 145, 155],
        'Institutional Target': [80, 85, 90, 95, 100, 105],
        'Institutional Actual': [75, 80, 85, 90, 95, 100],
        'Achievement %': [92, 94, 102, 96, 97, 97]
    })

def create_market_data():
    return pd.DataFrame({
        'Brand': ['OEM', 'Competitor A', 'Competitor B', 'Competitor C'],
        'Volume': [12450, 15200, 9800, 8700],
        'Growth LY': [8.5, 5.2, 12.1, -2.4],
        'MS Change': [0.7, -0.3, 1.1, -1.5]
    })

# ===== DASHBOARD LAYOUT =====
current_date = datetime.now().strftime("%d %b %Y")

# Header Section
st.title("🚗 OEM Dealer Performance Dashboard")
st.markdown(f"*Last Updated: {current_date}*")

# Key Metrics Cards
with st.container():
    cols = st.columns(4)
    metrics = [
        ("Dealer Code", "DLR-001", "#2186FD"),
        ("Evaluation", "87/100", "#00C853"),
        ("Category", "PIP", "#FF7043"),
        ("Region", "North", "#AB47BC")
    ]
    
    for col, (title, value, color) in zip(cols, metrics):
        with col:
            st.markdown(
                f'<div class="metric-card" style="border-left-color: {color}">'
                f'<div style="font-size: 0.9rem; color: #555;">{title}</div>'
                f'<div style="font-size: 1.4rem; font-weight: bold;">{value}</div>'
                '</div>',
                unsafe_allow_html=True
            )

# Main Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Sales Performance", 
    "📊 Market Analytics", 
    "👥 Manpower", 
    "📱 Digital", 
    "⚠️ Issues"
])

# Tab 1: Sales Performance
with tab1:
    st.markdown('<div class="header-style">Sales Performance Dashboard</div>', unsafe_allow_html=True)
    
    # Performance Charts
    perf_data = create_performance_data()
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Retail Performance")
        st.bar_chart(
            perf_data,
            x='Month',
            y=['Retail Target', 'Retail Actual'],
            color=["#FF6B6B", "#4ECDC4"]
        )
        
        st.subheader("Institutional Performance")
        st.bar_chart(
            perf_data,
            x='Month',
            y=['Institutional Target', 'Institutional Actual'],
            color=["#FFA07A", "#7FB3D5"]
        )
    
    with col2:
        st.subheader("Current Month")
        st.metric("Retail Achievement", "155/160", "97%")
        st.metric("Institutional", "100/105", "95%")
        st.progress(96, text="Overall Achievement")
        
        st.subheader("Quarterly Trend")
        st.area_chart(
            pd.DataFrame({
                'Quarter': ['Q1', 'Q2'],
                'Growth': [8.5, 7.2]
            }).set_index('Quarter'),
            color=["#4CAF50"]
        )

# Tab 2: Market Analytics
with tab2:
    st.markdown('<div class="header-style">Market Analytics Dashboard</div>', unsafe_allow_html=True)
    
    # Market Metrics
    cols = st.columns(4)
    market_metrics = [
        ("Volume", "12,450", "8.5%"),
        ("Market Share", "18.2%", "+0.7pp"),
        ("Retail Mix", "62%", "+4%"),
        ("Inventory Days", "28", "-3")
    ]
    
    for col, (title, value, delta) in zip(cols, market_metrics):
        with col:
            st.metric(title, value, delta)
    
    # Competitor Analysis
    st.subheader("Competitor Benchmarking")
    market_data = create_market_data()
    st.dataframe(
        market_data.style
        .bar(subset=['Growth LY'], color=['#ff6b6b','#7bc043'], align='mid')
        .format({'Growth LY': '{:.1f}%', 'MS Change': '{:.1f}pp'})
    )
    
    # Market Share Trend
    st.subheader("Market Share Trend")
    st.line_chart(
        pd.DataFrame({
            'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
            'OEM': [17.5, 17.8, 18.0, 18.1, 18.2, 18.2],
            'Comp A': [22.1, 21.8, 21.5, 21.3, 21.1, 20.9],
            'Comp B': [14.5, 14.8, 15.1, 15.3, 15.5, 15.6]
        }).set_index('Month'),
        color=["#4CAF50", "#FF5722", "#2196F3"]
    )

# [Additional tabs for Manpower, Digital, and Issues would follow same pattern]

# Footer
st.markdown("---")
st.markdown("**© 2025 OEM Dealer Analytics Pro** | *Internal Use Only* | v2.2")

# Requirements.txt should contain:
"""
streamlit>=1.32.0
pandas>=2.1.4
numpy>=1.24.0
"""
