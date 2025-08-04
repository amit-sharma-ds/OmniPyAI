import streamlit as st
from translate import Translator

st.set_page_config(page_title="Language Translator", layout="centered")
st.header("🌐 Language Translator (Offline)")

# Full language name to ISO code mapping
lang_map = {
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese (Simplified)": "zh",
    "Japanese": "ja",
    "Arabic": "ar",
    "Russian": "ru",
    "Portuguese": "pt",
    "Italian": "it",
    "Korean": "ko",
    "Turkish": "tr",
    "Dutch": "nl"
}

# UI
text = st.text_area("Enter text to translate:")
target_lang_name = st.selectbox("Select target language", list(lang_map.keys()))

if st.button("Translate"):
    try:
        target_lang_code = lang_map[target_lang_name]
        translator = Translator(to_lang=target_lang_code)
        translated = translator.translate(text)
        st.success(f"**Translated Text:**\n\n{translated}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
