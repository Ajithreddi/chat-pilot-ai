# **ChatPilot AI**

### *A free, safe, and smart AI assistant for learners — powered by Streamlit, AI agents, and n8n.*

[![Live App](https://img.shields.io/badge/Live%20App-ChatPilot%20AI-ff4b4b?logo=streamlit\&logoColor=white)](https://ajith-chatpilot.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)]()
[![n8n](https://img.shields.io/badge/Automation-n8n-orange?logo=n8n)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]()
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)]()

---

## 🎯 Overview

**ChatPilot AI** is a production-ready AI learning assistant designed to deliver:

* Homework help
* Concept explanations
* Doubt-solving
* Fast, reliable answers

It combines:

* A **Streamlit frontend**,
* A backend powered by **LLMs (OpenAI / Gemini)**, and
* **Automation + memory** using **n8n AI Agents**.

This architecture makes ChatPilot AI scalable, maintainable, and easy to extend.

---

## 🚀 Live Demo

👉 **Use ChatPilot AI:**
[https://ajith-chatpilot.streamlit.app/](https://ajith-chatpilot.streamlit.app/)

---

## 🧩 Architecture Overview

ChatPilot AI uses an **event-driven design** powered by n8n:

* Incoming requests from the Streamlit app are sent to an **n8n Webhook**
* n8n routes the request through an **AI Agent**
* The agent uses:

  * A **Google Gemini / Chat Model**
  * **n8n Simple Memory** to maintain context
  * Optional **tools** (custom functions / APIs)
* n8n sends a structured response back to Streamlit

### 🔧 n8n Workflow

Below is the workflow you provided (embedded directly):

![n8n workflow diagram](/mnt/data/7a091f19-5933-4f36-bc92-4f7aaf52faa1.png)

---

## 🛠️ Tech Stack

| Layer      | Technology                     |
| ---------- | ------------------------------ |
| Frontend   | Streamlit                      |
| Backend    | Python                         |
| AI Model   | Gemini / OpenAI (configurable) |
| Automation | n8n AI Agent + Webhook         |
| Memory     | n8n Simple Memory              |
| Deployment | Streamlit Cloud                |

---

## 📁 Project Structure

```
chat-pilot-ai/
│
├── app.py               # Main Streamlit UI + API interaction
├── config.py            # Webhook URL, model config, system prompts
├── requirements.txt     # Python dependencies
├── .gitignore           # Ignore rules for environment files & system data
└── README.md            # Documentation
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ajithreddi/chat-pilot-ai
cd chat-pilot-ai
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file (not committed to GitHub):

```
OPENAI_API_KEY=your_api_key
N8N_WEBHOOK_URL=https://your-n8n-instance/webhook/chatpilot
MODEL_NAME=gemini-pro   # or gpt-4o-mini, etc.
```

### 4️⃣ Start the App

```bash
streamlit run app.py
```

The app will open automatically in your browser at:

```
http://localhost:8501
```

---

## 🔌 n8n Integration

### Your n8n Workflow Includes:

1. **Webhook Trigger** – receives message from Streamlit
2. **AI Agent Node** – built-in n8n agent with:

   * Chat Model
   * Memory
   * Optional Tools
3. **Respond to Webhook** – returns the AI answer to Streamlit

### Why n8n?

* Centralizes prompt logic
* Offers persistent memory
* Easy to add tools (math, API calls, DB lookups, etc.)
* Enables logging, monitoring, retries, and scaling
* Low-code + AI-native agent features

---

## 🌐 Deployment

### Deploy on **Streamlit Cloud**

1. Push repo to GitHub
2. Go to: [https://share.streamlit.io](https://share.streamlit.io)
3. Create a new app
4. Add your `.env` values under **Secrets**
5. Deploy

### Deploy n8n

You can use:

* n8n Cloud
* Docker (`docker-compose`)
* Render
* Railway
* Local machine

Make sure your Streamlit app can reach your **public webhook URL**.

---

## 🔒 Security & Stability

* API keys stored only in environment variables
* Webhook URLs kept in `config.py` or `.env`
* Memory isolated per session
* n8n workflow logs help auditing
* Robust error handling in app.py
* MIT license allows safe open-source use

---

## 📌 Roadmap

* [ ] Implement multi-model selection
* [ ] Add conversation history UI
* [ ] Add image understanding support
* [ ] Add tool-based workflows (calculators, search, scraping)
* [ ] Add optional authentication for users

---

## 🤝 Contributing

Pull requests are welcome!
If you want new features or improvements, open an issue.

---

## 📄 License

Released under the **MIT License** — free for personal and commercial use.