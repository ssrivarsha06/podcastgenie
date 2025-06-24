import requests

API_KEY = "fbd924aca9d265d6faab0e10dabc8a8545600586726ea214f4e8ce6c970b4ca1"

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

    url = "https://api.together.xyz/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 1500
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        generated_script = response.json()["choices"][0]["message"]["content"]
        # Post-process to ensure correct format
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
        
        # If line ends with colon (speaker name), merge with next line
        if line.endswith(':') and (line.startswith('HOST') or line.startswith('GUEST')):
            if i + 1 < len(lines) and lines[i + 1].strip():
                # Merge speaker name with dialogue
                dialogue = lines[i + 1].strip()
                cleaned_lines.append(f"{line} {dialogue}")
                i += 2  # Skip next line since we merged it
            else:
                cleaned_lines.append(line)
                i += 1
        else:
            cleaned_lines.append(line)
            i += 1
    
    return '\n'.join(cleaned_lines)
