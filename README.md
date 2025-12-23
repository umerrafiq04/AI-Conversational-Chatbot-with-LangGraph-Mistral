# 🤖 AI Conversational Chatbot with LangGraph, Mistral & LangSmith

An AI-powered conversational chatbot built using **LangGraph**, **LangChain**, and **Mistral LLM**, featuring **multi-threaded conversation memory**, **persistent SQLite checkpointing**, **LangSmith observability**, and an interactive **Streamlit UI**.

This project demonstrates **state-based LLM orchestration**, **conversation-level memory management**, and **production-grade AI application practices**.

---

## ✨ Key Features

* 🧠 **State-based conversation flow** using LangGraph
* 💬 **Multi-threaded conversations** (each chat has its own memory)
* 💾 **Persistent memory** using SQLite checkpointer
* 🔄 **Conversation switching** via sidebar
* 🏷️ **Automatic conversation title generation**
* ⚡ **Real-time streaming AI responses**
* 🌐 **Interactive web UI** with Streamlit
* 🔍 **LangSmith tracing & observability**
* 🔐 **Secure API key management** using environment variables

---

## 🏗️ Architecture Overview

```
User (Browser)
    │
    ▼
Streamlit Frontend
    │
    ▼
LangGraph State Machine
    │
    ▼
Mistral LLM (ChatMistralAI)
    │
    ▼
SQLite Checkpointer (Persistent Memory)
    │
    ▼
LangSmith (Tracing & Monitoring)
```

---

## 📁 Project Structure

```
AI-Conversational-Chatbot-with-LangGraph-Mistral/
│
├── Frontend.py        # Streamlit user interface
├── Backend2.py        # LangGraph backend logic
├── chatbot.db         # SQLite database (auto-generated)
├── requirements.txt   # Python dependencies
├── .gitignore         # Ignored files
├── .env               # API keys (NOT committed)
└── README.md
```

---

## 🧠 How It Works

### 🔹 Backend (LangGraph)

* Uses a `StateGraph` to model the conversation as a state machine
* Each message updates the graph state
* Messages are stored using a **SQLite checkpointer**
* Conversations are isolated using a unique `thread_id`

### 🔹 Frontend (Streamlit)

* Sidebar lists all previous conversations
* Users can switch conversations instantly
* First few messages are summarized into a short conversation title
* Assistant responses are streamed token-by-token

---

## 🔍 LangSmith Integration (Tracing & Observability)

This project integrates **LangSmith** to enable deep visibility into LLM execution.

LangSmith provides:

* Prompt → response tracing
* LangGraph node execution inspection
* Latency and token usage tracking
* Debugging across conversation threads

---

### 🔧 LangSmith Environment Configuration

Add the following to your `.env` file:

```env
# Enable LangSmith tracing
LANGCHAIN_TRACING_V2=true

# LangSmith endpoint
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com

# LangSmith API key
LANGCHAIN_API_KEY=your_langsmith_api_key_here

# Project name shown in LangSmith dashboard
LANGCHAIN_PROJECT=chat bot with langsmith
```

⚠️ **Never commit real API keys to GitHub**

---

### 🛠️ How Tracing Works

Once enabled:

* All `llm.invoke()` calls are traced
* Each LangGraph node execution is recorded
* Conversation flows can be analyzed per thread

No additional code changes are required.

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/umerrafiq04/AI-Conversational-Chatbot-with-LangGraph-Mistral.git
cd AI-Conversational-Chatbot-with-LangGraph-Mistral
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key_here
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your_langsmith_api_key_here
LANGCHAIN_PROJECT=chat bot with langsmith
```

---

### 5️⃣ Run the Application

```bash
streamlit run Frontend.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🔐 Security Best Practices

* API keys are stored in `.env`
* `.env`, database files, and virtual environments are excluded via `.gitignore`
* No secrets are committed to version control

Example `.gitignore`:

```gitignore
.env
*.db
venv/
__pycache__/
```

---

## 📦 Tech Stack

| Layer         | Technology  |
| ------------- | ----------- |
| UI            | Streamlit   |
| LLM           | Mistral     |
| Orchestration | LangGraph   |
| Framework     | LangChain   |
| Memory        | SQLite      |
| Observability | LangSmith   |
| Language      | Python 3.12 |

---

## 🧪 Example Use Cases

* Persistent AI chat assistant
* Multi-session conversational agents
* LangGraph learning & experimentation
* LLM observability demonstrations
* Portfolio-ready AI engineering project

---

## 📌 Future Enhancements

* 🗑️ Delete / rename conversations
* 📄 Export chats to PDF
* 🐳 Dockerized deployment
* ☁️ Cloud hosting (Streamlit Cloud / Azure / AWS)
* 🔄 Replace SQLite with Redis / PostgreSQL
* 🧩 Tool & agent integrations

---

## 👨‍💻 Author

**Umer Rafiq**
BTech Computer Science & Engineering
AI & Web Development Enthusiast
📍 Kashmir, India

---

## ⭐ Support

If you found this project useful:

* Give it a ⭐ on GitHub
* Fork and extend it
* Share feedback or improvements

---

## 📣 Recruiter Note

> This project demonstrates hands-on experience with **LLM orchestration**, **state machines**, **persistent memory**, **streaming responses**, and **observability using LangSmith**, reflecting real-world AI system design practices.

---


