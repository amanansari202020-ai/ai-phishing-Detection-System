import streamlit as st
import joblib
import re

model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    return text

st.title("AI Phishing Detection System")

user_input = st.text_area("Enter Email or Message")

if st.button("Check"):
    if user_input.strip() == "":
        st.warning("Please enter some text")
    else:
        cleaned = clean_text(user_input)
        vector = vectorizer.transform([cleaned])
        prediction = model.predict(vector)

        if prediction[0] == 1:
            st.error("🚨 Phishing Email Detected")
        else:
            st.success("✅ Safe Email")