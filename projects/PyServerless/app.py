import streamlit as st
import pandas as pd
import altair as alt
import datetime

st.set_page_config(
    page_title="Stlite Starter Kit",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main .block-container {
        padding-top: 2.5rem;
        padding-bottom: 2rem;
    }
    .stButton > button {
        transition: all 0.2s ease-in-out;
    }
    .stButton > button:hover {
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)

if "counter" not in st.session_state:
    st.session_state.counter = 0

if "user_name" not in st.session_state:
    st.session_state.user_name = "Developer"

with st.sidebar:
    st.title("🚀 App Menu")
    page = st.radio("Navigation", ["Dashboard", "Data Explorer", "Settings"], label_visibility="collapsed")
    
    st.divider()
    st.markdown("**System Info**")
    st.caption("⚡ Running purely in-browser via WebAssembly.")
    st.caption(f"📅 Loaded on: {datetime.date.today().strftime('%B %d, %Y')}")

if page == "Dashboard":
    st.header("Home Dashboard")
    st.markdown("Welcome to the **Serverless Python Starter Kit**. This layout demonstrates a mock multi-page routing system, state management, and modern component alignment.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Active Sessions", "1,024", "+14.5%")
    col2.metric("Monthly Revenue", "$54,000", "-5.2%")
    col3.metric("System Load", "1.2ms", "Optimal", delta_color="off")
    
    st.divider()
    
    st.subheader("Global Session State Demo")
    st.write(f"Hello, **{st.session_state.user_name}**! Notice how your state persists when you switch pages.")
    
    cc1, cc2 = st.columns([1, 4])
    with cc1:
        if st.button("➕ Increment Value", use_container_width=True):
            st.session_state.counter += 1
    with cc2:
        st.info(f"The counter is currently at: **{st.session_state.counter}**")
        
    with st.expander("📝 View Source Code Notes"):
        st.code("""
        if "counter" not in st.session_state:
            st.session_state.counter = 0
            
        st.session_state.counter += 1
        """, language="python")

elif page == "Data Explorer":
    st.header("Data Visualizations")
    st.markdown("Streamlit flawlessly integrates with powerful libraries like `pandas` and `altair` directly in the browser.")
    
    data = pd.DataFrame({
        'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'Revenue': [15000, 18000, 22000, 21000, 25000, 30000],
        'Expenses': [12000, 13000, 14000, 13500, 15000, 18000]
    })

    melted_data = data.melt(id_vars='Month', var_name='Type', value_name='Amount')
    
    chart = alt.Chart(melted_data).mark_bar(opacity=0.9, cornerRadiusTopLeft=2, cornerRadiusTopRight=2).encode(
        x=alt.X('Type:N', title=None, axis=alt.Axis(labels=False, ticks=False)),
        y=alt.Y('Amount:Q', axis=alt.Axis(format='$~s', grid=True)),
        color=alt.Color('Type:N', scale=alt.Scale(domain=['Revenue', 'Expenses'], range=['#3b82f6', '#ef4444']), legend=alt.Legend(title=None)),
        column=alt.Column('Month:N', header=alt.Header(title=None, labelOrient='bottom')),
        tooltip=['Month', 'Type', alt.Tooltip('Amount:Q', format='$,.0f')]
    ).properties(width=100, height=380).configure_view(strokeOpacity=0)
    
    st.altair_chart(chart, use_container_width=True)
    
    st.write("Raw Data Access")
    st.dataframe(data, use_container_width=True, hide_index=True)

elif page == "Settings":
    st.header("Settings")
    st.write("Demonstrating form inputs and persistent preference updating.")
    
    st.subheader("Profile Profile")
    new_name = st.text_input("Update User Name", value=st.session_state.user_name)
    
    if st.button("Save Name Configuration"):
        st.session_state.user_name = new_name
        st.success(f"Name updated to '{new_name}'! Head back to the Dashboard to see the change persist globally.")
        
    st.divider()
    
    st.subheader("Mock Preferences")
    c1, c2 = st.columns(2)
    with c1:
        st.toggle("Enable Experimental Features")
        st.toggle("Dark Mode Enforcement")
    with c2:
        st.selectbox("Select Theme Accent", ["Blue", "Purple", "Green", "Orange"])
