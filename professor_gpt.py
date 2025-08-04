import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="sk-proj...")

st.header("📚 ProfessorGPT - Learn Anything")

prompt = st.text_input("What do you want to learn?")
if st.button("Teach Me") and prompt.strip():
    with st.spinner("Preparing your lecture..."):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Teach me: {prompt}"}
            ]
        )
        st.success("Here's your explanation:")
        st.write(response.choices[0].message.content)
