import requests

# Replace this with your actual Groq API key
API_KEY = "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"

def generate_podcast_script(topic):
    prompt = f"""
You are a podcast scriptwriter. Create a dialogue-style podcast script about "{topic}".

CRITICAL FORMAT REQUIREMENTS:
- Every speaker line MUST be: "SPEAKER: dialogue text" (speaker and text on SAME line)
- Use exactly these speaker names: "HOST" and "GUEST" (all caps)
- Never put speaker names on separate lines from their dialogue
- Keep sound effects on separate lines like [INTRO MUSIC]

EXAMPLE FORMAT (follow this exactly):
HOST: Welcome to Tech Talk! I'm excited to discuss this topic today.
GUEST: Thanks for having me! This is such an interesting subject.
[TRANSITION MUSIC]
HOST: So tell me, what's your take on this?
GUEST: Well, I think we need to consider several factors here.

Create a natural 3-minute conversation about "{topic}" with:
- Warm introduction by HOST
- Back-and-forth discussion between HOST and GUEST  
- Natural wrap-up
- Include [INTRO MUSIC] at start and [OUTRO MUSIC] at end
- Use conversational, friendly tone

Remember: ALWAYS format as "SPEAKER: dialogue" on the same line!
"""

    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-oss-20b",   # ✅ Updated supported model
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1500
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        generated_script = response.json()["choices"][0]["message"]["content"]
        print("🧾 RAW MODEL OUTPUT:\n", generated_script)  # 👀 debug line
        return clean_script_format(generated_script)
    else:
        return f"Error: {response.status_code} - {response.text}"

def clean_script_format(script):
    """Clean up script format to ensure speaker lines are properly formatted"""
    lines = script.split('\n')
    cleaned_lines = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if line.endswith(':') and (line.upper().startswith('HOST') or line.upper().startswith('GUEST')):
            if i + 1 < len(lines) and lines[i + 1].strip():
                dialogue = lines[i + 1].strip()
                cleaned_lines.append(f"{line} {dialogue}")
                i += 2
            else:
                cleaned_lines.append(line)
                i += 1
        else:
            cleaned_lines.append(line)
            i += 1

    return '\n'.join(cleaned_lines)
