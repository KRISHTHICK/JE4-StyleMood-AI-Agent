import streamlit as st
from stylist_agent import get_stylist_recommendation
from mood_utils import generate_moodboard, generate_caption
from PIL import Image

st.set_page_config(page_title="🧢 StyleMood AI", layout="wide")
st.title("🎨🧢 StyleMood AI – Fashion Moodboard & Stylist Agent")

st.markdown("Unleash your fashion creativity with an AI that styles you based on your **mood**, **vibe**, or **event**.")

# Input
mood = st.text_input("🧠 What's your mood today? (e.g. confident, cozy, romantic)")
style = st.text_input("👗 Any fashion preference? (e.g. streetwear, vintage, chic)")
event = st.text_input("🎉 Occasion or event? (e.g. brunch, interview, date night)")

uploaded_image = st.file_uploader("📸 Optional selfie or outfit photo", type=["jpg", "jpeg", "png"])
if uploaded_image:
    img = Image.open(uploaded_image)
    st.image(img, caption="Uploaded Inspiration", use_column_width=True)

if st.button("✨ Generate My Style Moodboard"):
    st.subheader("👚 Outfit Suggestion")
    st.write(get_stylist_recommendation(mood, style, event))

    st.subheader("🎨 Fashion Moodboard")
    st.write(generate_moodboard(mood, style))

    st.subheader("📝 Caption or Vibe Summary")
    st.write(generate_caption(mood, style))
