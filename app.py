import streamlit as st
import pandas as pd

st.title("Future Skills Radar — Data Analyst (India)")

skill_freq = pd.read_csv("Data/Processed/skill_frequency.csv")

st.subheader("Top Skills in the Market")
st.bar_chart(skill_freq.set_index("Skill")["Number_of_Postings"].head(15))

st.subheader("Check Your Skill Gap")
user_input = st.text_input("Apni skills comma se separate karke likho (e.g. Python, SQL, Excel)")

if user_input:
    user_skills = [s.strip().lower() for s in user_input.split(",")]
    top_n = 10
    top_skills = skill_freq.head(top_n)["Skill"].str.replace("_", " ").tolist()
    have = [s for s in top_skills if s.lower() in user_skills]
    missing = [s for s in top_skills if s.lower() not in user_skills]
    st.write(f"✅ Have: {', '.join(have) if have else 'Koi nahi abhi'}")
    st.write(f"❌ Missing: {', '.join(missing) if missing else 'Kuch nahi — badhiya!'}")
    st.write(f"📊 Coverage: {round(len(have)/top_n*100,1)}%")