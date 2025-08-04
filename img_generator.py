import streamlit as st
import openai

openai.api_key = "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"

st.header("🖼️ AI Image Generator")

prompt = st.text_input("Enter your image prompt:")
if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating..."):
            try:
                response = openai.Image.create(
                    prompt=prompt,
                    n=1,
                    size="512x512"
                )
                image_url = response['data'][0]['url']
                st.image(image_url, caption="Generated Image")
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a prompt.")
