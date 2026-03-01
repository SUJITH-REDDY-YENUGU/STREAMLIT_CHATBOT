
# 🤖 ChatGroq AI Chatbot with Streamlit

A robust chatbot built using **Streamlit**, **LangChain**, and **Groq API** with a modern frontend.  
This app lets you interact with Groq’s instant LLMs (e.g., `llama-3.1-8b-instant`, `llama-3.1-70b-instant`, `gemma2-9b-it`) through a clean chat interface.

---

## 🚀 Features
- Interactive chat interface with history (`st.chat_message`)
- Sidebar settings to choose model and adjust creativity (temperature)
- Powered by **LangChain + Groq LLMs**
- Secure API key management via `.env`

---

## 📂 Project Structure

```
chatgroq-chatbot/
├── main.py            # Streamlit app
├── .env               # Environment variables (API key)
├── requirements.txt   # Dependencies
└── README.md          # Documentation
```

---

## 🛠 Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/chatgroq-chatbot.git
   cd chatgroq-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Groq API key to `.env`:**
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the app:**
   ```bash
   streamlit run main.py
   ```

---

## ⚙️ Supported Models

The following models are currently supported by Groq:

- `llama-3.1-8b-instant`
- `llama-3.1-70b-instant`
- `gemma2-9b-it`

⚠️ If you see `model_not_found` errors, check your Groq console to confirm which models your API key has access to: [GroqCloud Models](https://console.groq.com/docs/models).

---

## 🌐 Deployment

You can deploy this app easily on **Streamlit Cloud**:
- Push your repo to GitHub
- Connect your repo on [Streamlit Cloud](https://streamlit.io/cloud)
- Add your `.env` secrets in the Streamlit dashboard

---

## 📜 License

MIT License. Free to use and modify.
```

---

