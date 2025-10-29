# 🎙️ AI Podcast Script + Voice Generator

An AI-powered tool that automatically generates 3-minute podcast scripts on any topic and converts them into realistic voice using TTS (Text-to-Speech) models.

---

## ✨ Features

- 🧠 **Script Generation** using GPT-4o (OpenAI)
- 🔊 **Realistic Voice** using ElevenLabs Text-to-Speech API
- 💻 **Streamlit UI** for an interactive experience
- 🧾 Automatically plays podcast audio in-browser

---

## 🧰 Tech Stack

| Layer            | Tool               |
|------------------|--------------------|
| Language Model   | GPT-4o (OpenAI)    |
| Text-to-Speech   | ElevenLabs API     |
| Web Interface    | Streamlit          |
| Language         | Python             |

---

## 🚀 How It Works

1. User enters a topic
2. GPT-4o generates a 3-minute conversational podcast script
3. ElevenLabs converts the script into realistic speech
4. The final podcast audio plays in the browser

---

## 📂 Folder Structure

podcastgenie/
├── app.py # Streamlit frontend
├── gpt_script.py # GPT-based script generator (edit API key here)
├── tts.py # ElevenLabs voice generator (edit API key here)
├── podcast_audio.mp3 # Output audio file
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment (optional)


---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone [https://github.com/yourusername/podcastgenie.git](https://github.com/ssrivarsha06/podcastgenie)
cd podcastgenie
```
### 2. Set Up Virtual Environment (optional but recommended)
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
🔐 Configure API Keys (IMPORTANT)
Since this version uses hardcoded API keys:

➤ In gpt_script.py
Find this line and replace with your actual OpenAI API key:
```
openai.api_key = "YOUR-API-KEY"
```
➤ In tts.py
Find this line and replace with your actual ElevenLabs API key:
```
api_key = "YOUR-ELEVENLABS-API-KEY"
```
▶️ Run the App
```
streamlit run app.py
```
Open the browser at http://localhost:8501

🧪 Sample Output
Topic: Is AI replacing human jobs?

GPT Script: 3-minute podcast-style script

Audio: MP3 voice output generated via ElevenLabs
🔮 Future Work
Add background music

Provide voice selection

Add download button for generated audio

Integrate Bark TTS as a fallback

Deploy publicly via Streamlit Cloud

📜 License
This project is built for educational use with Generative AI tools.


