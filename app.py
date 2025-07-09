import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

from db import init_db, add_or_update_entry, fetch_all

init_db()

st.set_page_config(page_title="Screen Time Dashboard", layout="wide")

st.title("Screen Time Tracker App")

# 📋 Input Form
with st.form("entry_form", clear_on_submit=True):
    st.subheader("Add or Update Today's Screen Time")
    c1, c2, c3 = st.columns(3)
    today = c1.date_input("Date", value=date.today())
    laptop = c2.slider("Laptop Time (hours)", min_value=0.0, max_value=24.0, step=0.25)
    phone = c3.slider("Phone Time (hours)", min_value=0.0, max_value=24.0, step=0.25)
    submitted = st.form_submit_button("Submit")
    if submitted:
        add_or_update_entry(today, laptop, phone)
        st.success(f"Data for {today} saved.")

st.markdown("---")

# 📊 Fetch Data
df = fetch_all()
if df is None or df.empty:
    st.info("No data yet. Add today's screen time above.")
    st.stop()

df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# 🔷 KPIs
total_laptop = df['laptop_time'].sum()
total_phone = df['phone_time'].sum()
avg_laptop = df['laptop_time'].mean()
avg_phone = df['phone_time'].mean()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Laptop Time", f"{total_laptop:.1f} hrs", help="Total laptop usage")
kpi2.metric("Total Phone Time", f"{total_phone:.1f} hrs", help="Total phone usage")
kpi3.metric("Avg Laptop / Day", f"{avg_laptop:.1f} hrs", help="Average laptop per day")
kpi4.metric("Avg Phone / Day", f"{avg_phone:.1f} hrs", help="Average phone per day")

st.markdown("---")

# 📑 Tabs for Data and Charts
tab1, tab2, tab3 = st.tabs(["Trends", "Comparison", "Data Table"])

with tab1:
    st.subheader("Time Series Trends")
    fig = px.line(
        df,
        x='date',
        y=['laptop_time', 'phone_time'],
        labels={'value': 'Hours', 'date': 'Date', 'variable': 'Device'},
        markers=True,
        color_discrete_map={
            'laptop_time': 'green',
            'phone_time': 'orange'
        }
    )
    fig.update_layout(legend_title_text='Device')
    st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("📊 Daily Comparison")
    fig_bar = px.bar(
        df,
        x='date',
        y=['laptop_time', 'phone_time'],
        labels={'value': 'Hours', 'date': 'Date', 'variable': 'Device'},
        barmode='group',
        color_discrete_map={
            'laptop_time': 'green',
            'phone_time': 'orange'
        }
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab3:
    st.subheader("aw Data Table")
    st.dataframe(df.style.format({"laptop_time": "{:.2f}", "phone_time": "{:.2f}"}))

st.markdown("---")
st.caption("Built with ❤️ by Pritam. On 9th July, 2025")
