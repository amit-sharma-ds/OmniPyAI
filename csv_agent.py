import streamlit as st
import pandas as pd

st.set_page_config(page_title="📊 CSV Analyzer", layout="centered")
st.title("📊 CSV Analyzer (Offline)")

csv_file = st.file_uploader("Upload CSV File", type=["csv"])

if csv_file:
    df = pd.read_csv(csv_file)
    st.success("✅ File uploaded successfully!")
    st.dataframe(df)

    col = st.selectbox("Select a column for stats", df.columns)

    if st.button("Show Stats"):
        st.write("🔍 Summary Statistics:")
        st.write(df[col].describe())
