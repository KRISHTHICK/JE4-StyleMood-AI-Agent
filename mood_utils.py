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
