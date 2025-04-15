import streamlit as st
from recommendation_engine import recommend_schedule
from load_data import load_company_data, load_event_attendance_data

st.set_page_config(page_title="VMSC Event Dashboard", layout="wide")
st.title("VMSC Event Recommendation")

df_events = load_event_attendance_data()
df_companies = load_company_data()

st.subheader("Event Attendance Data")
st.dataframe(df_events)

st.subheader("Company Visit Data")
st.dataframe(df_companies)

st.header("Recommended Event Strategy:")
recommendations = recommend_schedule(df_events)
st.markdown(f"Best Day of the Week: {recommendations['best_day']}")
st.markdown(f"Best Month: {recommendations['best_month']}")
st.markdown(f"Most Successful Event Type: {recommendations['best_type']}")
