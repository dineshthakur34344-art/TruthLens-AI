
import streamlit as st
import joblib

model = joblib.load("truthlens_model.pkl")

st.set_page_config(
    page_title="TruthLens AI",
    page_icon="🔎",
    layout="centered"
)

st.title("🔎 TruthLens AI")
st.subheader("Fake News Detection System")

st.write(
    "Enter a news article below and let our AI model analyse its text."
)

news = st.text_area("Paste your news article here:")

if st.button("Check News"):
    if news.strip():
        prediction = model.predict([news])[0]

        if prediction == "FAKE":
            st.error("⚠️ AI Prediction: FAKE")
        else:
            st.success("✅ AI Prediction: REAL")

    else:
        st.warning("Please enter some news text.")

st.divider()

st.caption(
    "Disclaimer: This is an educational AI classifier. "
    "Its prediction is not proof that a news story is true or false. "
    "Always verify important information using reliable sources."
)
