import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
HEADERS = {
    "Authorization": "Bearer (HF Token, Generate and Place here)"  # Replace with your actual Hugging Face token
}

def generate_rizz(user_message):
    prompt = f"""You are RizzBot — a confident, respectful, and charming AI wingman.
A girl says: "{user_message}"
Reply with a short, flirty, and smooth message to impress her."""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 100,
            "temperature": 0.9,
            "top_p": 0.95
        }
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            return result[0]["generated_text"].replace(prompt, "").strip()
        elif isinstance(result, dict) and "generated_text" in result:
            return result["generated_text"].replace(prompt, "").strip()
        elif isinstance(result, dict) and "error" in result:
            return f"Error: {result['error']}"
        else:
            return "No reply generated."
    except Exception as e:
        return f"Error: {str(e)}"







