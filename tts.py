import os
import re
import shutil
from elevenlabs import generate, save, set_api_key
from pydub import AudioSegment

# Set ElevenLabs API Key
set_api_key("sk_2f9c551fc4207b3ac823ea06b8500e1fd46e5d5228160142")

# Voice IDs
VOICE_IDS = {
    "host": "W78pxv1enhu0qj6t6IaC",   # Adam
    "guest": "XJa38TJgDqYhj5mYbSJA"  # Bella
}

# Sound effect file paths (UPDATE THESE PATHS)
SOUND_EFFECTS = {
    "[INTRO MUSIC]": "audio/intromusic.mp3",        # Add your intro file path
            # Optional
}

def clean_text(text):
    return text.strip().replace("“", '"').replace("”", '"')

def get_voice_id(speaker):
    speaker = speaker.lower()
    return VOICE_IDS.get(speaker, VOICE_IDS["host"])

def generate_voice(script_text):
    # Clean temp dir
    shutil.rmtree("temp_audio", ignore_errors=True)
    os.makedirs("temp_audio", exist_ok=True)
    
    audio_segments = []
    part_count = 0

    for line in script_text.strip().splitlines():
        line = line.strip()

        # Handle sound effects
        if line in SOUND_EFFECTS:
            sfx_path = SOUND_EFFECTS[line]
            if os.path.exists(sfx_path):
                print(f"🔊 Adding {line}")
                sfx = AudioSegment.from_file(sfx_path)
                audio_segments.append(sfx)
            else:
                print(f"⚠️ Missing file: {sfx_path}")
            continue

        # Skip empty lines and sound markers
        if not line or (line.startswith("[") and line.endswith("]")):
            continue

        # Match speaker line
        match = re.match(r"^(Host|Guest):\s*(.+)", line, re.IGNORECASE)
        if match:
            speaker, content = match.groups()
            content = clean_text(content)
            voice_id = get_voice_id(speaker)

            print(f"🔊 Generating for {speaker.title()}: {content}")
            audio = generate(text=content, voice=voice_id)
            filename = f"temp_audio/part{part_count}.mp3"
            save(audio, filename)
            audio_segments.append(AudioSegment.from_file(filename, format="mp3"))
            part_count += 1

    if not audio_segments:
        raise Exception("❌ No valid speaker lines found.")

    # Combine all audio segments
    final_audio = audio_segments[0]
    for segment in audio_segments[1:]:
        final_audio += segment

    final_audio.export("podcast_audio.mp3", format="mp3")
    print("✅ Exported podcast_audio.mp3")
