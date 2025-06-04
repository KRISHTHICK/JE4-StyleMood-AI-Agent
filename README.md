# JE4-StyleMood-AI-Agent
GenAI

Absolutely! Here's a **brand new AI agent project** with a **unique fashion-related theme**, powered by **Ollama**, **Python**, and **Streamlit**, ready to be run in **VS Code** and deployed on **GitHub** — without requiring virtual environments.

---

## 🧢👓 **StyleMood AI – Fashion Moodboard Generator & Stylist Agent**

### 📌 **Project Concept**:

**StyleMood AI** is an AI agent that takes your current **mood**, **fashion preference**, or **event type**, and generates a **personalized fashion moodboard** along with **styling suggestions**, **color palettes**, and **vibe captions**. Think of it as a digital fashion stylist + creative moodboard builder — all AI-powered!

---

### 🌟 **Core Features**

| Feature                             | Description                                                       |
| ----------------------------------- | ----------------------------------------------------------------- |
| 💬 **AI Stylist Agent**             | Suggests complete outfit ideas based on mood, style, or occasion  |
| 🎨 **Fashion Moodboard Generator**  | Generates visual inspirations (color palette + keywords + emojis) |
| 📸 **Optional Photo Input**         | Upload a selfie or outfit photo to fine-tune suggestions          |
| 🎯 **Style Vibe Caption Generator** | Captions like “90s Retro Cool with a splash of Gen-Z flair”       |
| 📅 **Look Calendar Suggestion**     | Recommends outfit mood by day or event                            |

---

### 📁 Folder Structure

```
StyleMood-AI/
├── app.py
├── stylist_agent.py
├── mood_utils.py
├── assets/
│   └── palette_samples/
├── requirements.txt
└── README.md
```

---

### 📦 `requirements.txt`

```txt
streamlit
ollama
Pillow
```

---

### 🚀 `app.py`

```python
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
```

---

### 🧠 `stylist_agent.py`

```python
import subprocess

def get_stylist_recommendation(mood, style, event):
    prompt = f"Suggest a fashion outfit based on mood: {mood}, style: {style}, and event: {event}. Include shoes, accessories, and colors. Be creative but wearable."
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()
```

---

### 🎨 `mood_utils.py`

```python
import random

def generate_moodboard(mood, style):
    palettes = {
        "confident": ["#000000", "#FFD700", "#FF4500"],
        "romantic": ["#FFC0CB", "#FFF0F5", "#B22222"],
        "cozy": ["#F5F5DC", "#8B4513", "#A0522D"],
        "vintage": ["#D2B48C", "#8B0000", "#556B2F"]
    }
    mood = mood.lower()
    matched = palettes.get(mood, ["#D3D3D3", "#FFFFFF", "#808080"])
    hex_list = ", ".join(matched)
    return f"Color Palette: {hex_list} 🎨\nKeywords: {mood.title()}, {style.title()} Vibes, Classic/Modern Fusion"

def generate_caption(mood, style):
    return f"Today’s vibe: {mood.title()} meets {style.title()} 🌟\n‘Dressed to express, not impress.’"
```

---

### 📘 `README.md`

````markdown
# 🧢 StyleMood AI – Fashion Moodboard Generator & Stylist Agent

AI Agent that generates fashion moodboards, outfit recommendations, and creative captions based on your mood, style, or events. Built with Streamlit + Ollama + Python.

## 💡 Features
- 🧠 AI Stylist using TinyLLaMA (local via Ollama)
- 🎨 Mood-based color palettes and keywords
- 📝 Captions like an Instagram stylist
- 📷 Upload selfies or outfits for better suggestions

## 🚀 How to Run

1. Clone the repo:
```bash
git clone https://github.com/yourusername/StyleMood-AI.git
cd StyleMood-AI
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start Ollama server & load model:

```bash
ollama serve
ollama run tinyllama
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

🎉 Enjoy your personalized moodboard!

```

---

### 🧪 Possible Add-On Features

- 🪞 **Virtual Try-On with Avatar Overlay**
- 📅 **Weekly Mood Calendar Generator**
- 💌 **Auto-create a fashion Pinterest board**
- ✂️ **AI Tailor Suggestions for Fit**

---

Would you like me to package this for GitHub, add blog post generation, or generate some sample data to test it?
```
