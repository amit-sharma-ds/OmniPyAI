import streamlit as st
from textblob import TextBlob

st.header("❤️ Sentiment Analyzer (Offline)")

text = st.text_area("Enter text to analyze:")

if st.button("Analyze"):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0:
        st.success("😊 Positive Sentiment")
    elif polarity < 0:
        st.error("☹️ Negative Sentiment")
    else:
        st.info("😐 Neutral Sentiment")
