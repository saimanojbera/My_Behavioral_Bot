# 🤖 Saimanoj's Behavioral Bot

This is a personalized voice-enabled chatbot designed as part of the Stage 1 interview assessment for the **Generative AI Developer** role at **Home.LLC**. The bot answers behavioral questions as *Saimanoj Bera*, leveraging a structured JSON profile and OpenAI’s GPT-4 API, all wrapped in a conversational chat interface using Streamlit.

---

## 🚀 Live Demo

👉 **App Link**: [https://my-behavioral-bot.streamlit.app](#)  
💬 Try asking questions like:
- "What’s your #1 superpower?"
- "What motivates you in your work?"
- "Tell me about a time you solved a problem creatively."

---

## 🧠 Features

- 💬 Conversational UI using `st.chat_message` (Streamlit's official chat framework)
- 🔊 Text-to-Speech integration using `pyttsx3`
- 🧾 Structured prompt injection from `my_story.json` for accurate, human-like answers
- 🎯 Suggested behavioral questions interface
- ⚡ Powered by OpenAI GPT-4 + Streamlit

---

## 📂 Project Structure

```
├── main.py                     # Streamlit app entry point
├── my_story.json              # Personal profile used in GPT prompt
├── requirements.txt           # Python dependencies
└── .streamlit/
    └── secrets.toml           # OpenAI API key for local use
```

---

## 🛠️ Running Locally

1. **Clone this repo**

```bash
git clone https://github.com/saimanojbera/My_Behavioral_Bot.git
cd My_Behavioral_Bot
```

2. **(Optional) Create a virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your OpenAI API Key**

Create a file at `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

5. **Run the app**

```bash
streamlit run main.py
```

---

## 🌐 Deploying to Streamlit Cloud

1. Push your code to a GitHub repo
2. Go to [https://share.streamlit.io](https://share.streamlit.io)
3. Add the following to **Secrets** in the UI:

```toml
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

4. Your app is now live via a shareable link ✅

---

## 🧾 Sample `my_story.json`

```json
{
  "identity": "Engineer by heart, creative problem solver, structured thinker.",
  "life_story": "Grew up in a small town. Transitioned from data engineering to AI. Completed Master's from University of Michigan.",
  "superpower": "Synthesizing complex ideas into clear insights.",
  "growth_areas": ["Leadership", "Prompt Engineering", "Prioritization"],
  "misconception": "People think I’m serious — I’m playful once you know me.",
  "boundary_pushing": "I build weekend AI projects & learn new tools rapidly.",
  "motivation": "Building tools that make others more efficient and creative.",
  "colleague_feedback_summary": "Reliable, thoughtful, methodical, shows up under pressure."
}
```

---

## 👤 About the Developer

Hi! I'm **Saimanoj Bera** — an AI engineer passionate about building meaningful systems that blend logic and empathy. This voice bot is a reflection of who I am — both technically and personally.

- 📧 [saimanoj2509@gmail.com](mailto:saimanoj2509@gmail.com)  
- 🔗 [LinkedIn](https://www.linkedin.com/in/saimanoj-bera-044831150/)  
- 🌐 [Portfolio](https://saimanojbera.github.io/)

---

## 📄 License

This project is part of a private interview assignment. Please do not reuse without permission.
