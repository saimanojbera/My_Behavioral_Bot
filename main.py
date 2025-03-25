import streamlit as st
from openai import OpenAI
import json
import random
import os
from gtts import gTTS
import tempfile

# Initialize OpenAI client securely using Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Load raw JSON string
def load_story_json_raw():
    try:
        with open('my_story.json', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "Error: my_story.json not found."
    except Exception as e:
        return f"Error loading JSON: {str(e)}"

def generate_system_prompt():
    story_json_raw = load_story_json_raw()
    return f"""
You are Saimanoj Bera, applying for the Generative AI Developer role at Home.LLC.
Respond to behavioral questions as Saimanoj would — with warmth, humility, and thoughtfulness.
Use the following personal story and information in raw JSON format to guide your responses:

{story_json_raw}

Keep responses short (<60 sec), grounded in real experience, and reflective. No fluff. Be real.
"""

def get_gpt_response(user_input):
    system_prompt = generate_system_prompt()
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Cloud-compatible voice output using gTTS
def speak(text):
    try:
        tts = gTTS(text)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmpfile:
            tts.save(tmpfile.name)
            st.audio(tmpfile.name, format="audio/mp3")
    except Exception as e:
        st.warning(f"Voice generation failed: {e}")

# UI Starts Here
def main():
    st.set_page_config(page_title="Saimanoj's Behavioral Bot", layout="centered")
    st.title("🤖 Saimanoj's Voice Bot")
    st.caption("Ask a behavioral interview question — via text — and get a voice + text response!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display previous chat history
    for entry in st.session_state.chat_history:
        with st.chat_message(entry["role"]):
            st.markdown(entry["content"])

    # Suggested Questions
    suggested_questions = [
        "What’s your #1 superpower?",
        "What are the top 3 areas you’d like to grow in?",
        "What misconception do your coworkers have about you?",
        "How do you push your boundaries and limits?",
        "What should we know about your life story in a few sentences?",
        "Why do you want to work with Home.LLC?",
        "What motivates you in your work?",
        "Tell me about a time you solved a problem creatively.",
        "Tell me about a time when you had an issue with a colleague."
    ]

    with st.expander("💡 Suggested Questions", expanded=True):
        cols = st.columns(4)
        for i, q in enumerate(random.sample(suggested_questions, 4)):
            if cols[i % 4].button(q):
                st.session_state.user_input = q

    # Input
    prompt = st.chat_input("Type your question here...")
    user_message = None

    if prompt:
        user_message = prompt
    elif "user_input" in st.session_state and st.session_state.user_input:
        user_message = st.session_state.user_input
        st.session_state.user_input = ""

    if user_message:
        st.session_state.chat_history.append({"role": "user", "content": user_message})
        with st.chat_message("user"):
            st.markdown(user_message)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = get_gpt_response(user_message)
                st.markdown(response)
                speak(response)  # Voice output using gTTS

        st.session_state.chat_history.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
