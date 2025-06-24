import streamlit as st
from gpt_script import generate_podcast_script
from tts import generate_voice

st.set_page_config(page_title="🎙️ AI Podcast Generator", layout="centered")

st.title("🎙️ Realistic AI Podcast with Two Voices")
st.markdown("Enter a topic to generate a **natural podcast** with Host & Guest voices.")

topic = st.text_input("🎧 Podcast Topic:")

if st.button("Generate Podcast"):
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("📝 Generating podcast script..."):
            script = generate_podcast_script(topic)
            st.subheader("📜 Podcast Script")
            st.text_area("Preview", script, height=300)

        with st.spinner("🎙️ Converting to voice..."):
            try:
                generate_voice(script)
                st.success("✅ Podcast audio generated!")
                st.audio("podcast_audio.mp3", format="audio/mp3")
            except Exception as e:
                st.error(f"Error: {e}")
