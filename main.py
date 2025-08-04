import streamlit as st

st.set_page_config(page_title="OmniPyAI", layout="centered")
st.title("🤖 OmniPyAI - All-in-One AI Assistant")
st.markdown("**One App. Infinite AI Power — Built with Pure Python.**")

st.sidebar.title("Navigation")
choice = st.sidebar.radio("Choose a Tool", [
    "ProfessorGPT",
    "To-Do List",
    "BMI Calculator",
    "AI Image Generator",
    "Language Translator",
    "CSV Agent",
    "Sentiment Analyzer"
])

if choice == "ProfessorGPT":
    exec(open("professor_gpt.py", encoding="utf-8").read())
elif choice == "To-Do List":
    exec(open("todo.py", encoding="utf-8").read())
elif choice == "BMI Calculator":
    exec(open("bmi_calc.py", encoding="utf-8").read())
elif choice == "AI Image Generator":
    exec(open("img_generator.py", encoding="utf-8").read())
elif choice == "Language Translator":
    exec(open("translator.py", encoding="utf-8").read())
elif choice == "CSV Agent":
    exec(open("csv_agent.py", encoding="utf-8").read())
elif choice == "Sentiment Analyzer":
    exec(open("sentiment.py", encoding="utf-8").read())
