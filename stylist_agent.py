import subprocess

def get_stylist_recommendation(mood, style, event):
    prompt = f"Suggest a fashion outfit based on mood: {mood}, style: {style}, and event: {event}. Include shoes, accessories, and colors. Be creative but wearable."
    result = subprocess.run(["ollama", "run", "tinyllama", prompt], capture_output=True, text=True)
    return result.stdout.strip()
