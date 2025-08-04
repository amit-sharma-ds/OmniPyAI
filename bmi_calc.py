import streamlit as st

st.header("⚖️ BMI Calculator")

height = st.slider("Enter your height (cm)", 100, 250, 170)
weight = st.slider("Enter your weight (kg)", 30, 200, 70)

bmi = weight / ((height / 100) ** 2)
st.write(f"Your BMI is: **{bmi:.2f}**")

st.markdown("### BMI Categories")
st.markdown("- Underweight: < 18.5")
st.markdown("- Normal: 18.5 – 24.9")
st.markdown("- Overweight: 25 – 29.9")
st.markdown("- Obese: ≥ 30")
