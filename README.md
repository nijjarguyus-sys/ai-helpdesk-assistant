# 💻 AI Help Desk Assistant

An AI-powered IT support assistant designed to help users troubleshoot common technical issues quickly and efficiently.

## 🚀 Project Overview

The AI Help Desk Assistant is a web-based application built with Python and Streamlit.

The goal of this project is to demonstrate how Artificial Intelligence can improve IT support operations by providing instant troubleshooting guidance for common user problems.

## 🎯 Business Problem

Many organizations receive repetitive IT support requests:

- Password reset issues
- VPN connectivity problems
- Printer problems
- Email configuration issues
- Network connectivity problems

This project explores how AI can reduce support workload and improve response time.

## ✨ Features

Current features:

✅ Interactive web interface  
✅ IT issue selection menu  
✅ Automated troubleshooting responses  
✅ Simple and user-friendly design  


## 🔄 Application Pipeline

The AI Help Desk Assistant uses a knowledge-base-first architecture with an AI fallback mechanism.

```text
                         ┌──────────────────────┐
                         │      User Query      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                    ┌────────────────────────────┐
                    │   Input Processing Layer   │
                    │                            │
                    │ • Chat Input               │
                    │ • Suggested Questions      │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │      Knowledge Base        │
                    │       (FAQ / JSON)         │
                    └─────────────┬──────────────┘
                                  │
                         ┌────────┴────────┐
                         │                 │
                       Found            Not Found
                         │                 │
                         ▼                 ▼
                ┌────────────────┐  ┌────────────────┐
                │ Knowledge Base │  │    Groq AI     │
                │    Response    │  │   Fallback     │
                └───────┬────────┘  └───────┬────────┘
                        │                   │
                        └─────────┬─────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │      Assistant Response    │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │    Session Chat History    │
                    │                            │
                    │ • Message Counter          │
                    │ • Clear Chat               │
                    │ • Export Chat              │
                    └────────────────────────────┘
                    Pipeline Overview
User Query – The user enters an IT support question or selects a suggested question.
Input Processing – The application receives and processes the question through the Streamlit interface.
Knowledge Base Search – The application checks the local IT FAQ/knowledge base first.
Knowledge Base Response – If a matching answer is found, the stored response is returned.
Groq AI Fallback – If no relevant knowledge-base answer is found, the question is sent to the Groq API for an AI-generated response.
Assistant Response – The response is displayed in the chat interface.
Conversation Management – User and assistant messages are stored in Streamlit session state.
Chat Utilities – Users can view the message count, clear the conversation, or export the chat as a text file.


## 🛠️ Technology Stack

- **Language:** Python
- **Frontend/UI:** Streamlit
- **AI:** Groq API
- **Knowledge Base:** JSON
- **Environment Management:** Python-dotenv
- **Version Control:** Git & GitHub
- **Development Environment:** VS Code

## 📂 Project Structure

[AI-HelpDesk-Assistant/

│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── assets/
├── data/
└── prompts/
│__utils

📸 Screenshots
## App Preview

![IT Helpdesk Assistant app](assets/screenshots/app-preview.png)

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/nijjarguyus-sys/ai-helpdesk-assistant.git
Navigate into the project:

cd ai-helpdesk-assistant

Create virtual environment:

python -m venv .venv

Activate environment:

Windows:

.\.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt

Run application:

streamlit run app.py
<<<<<<< HEAD
📸 Screenshots
## App Preview

![IT Helpdesk Assistant](assets/screenshots/app-preview.png)

=======

## 🔐 Environment Variables

The application uses an environment variable to securely store the Groq API key.

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here


## ▶️ Usage


## AI Provider

The application uses the **Groq API** for AI-powered responses.

The project was initially developed with the Gemini API. Due to API quota limitations during development, the AI integration was migrated to Groq with minimal architectural changes.
## ✨ Features

- 💻 Interactive Streamlit web interface
- 🔧 Common IT troubleshooting services
- 📚 Local IT knowledge base / FAQ
- 🤖 Groq-powered AI fallback
- 💡 Suggested IT questions
- 💬 Conversation history
- 📊 Dynamic message counter
- 🗑️ Clear chat functionality
- 📥 Export conversation as a text file
- 🔐 API keys managed through environment variables


## 🔮 Future Improvements

- Add advanced retrieval using vector embeddings
- Improve knowledge-base matching
- Add AI response source indicators
- Add ticket creation and tracking
- Deploy using cloud services
- Add analytics dashboard
- Add automated evaluation of AI responses
- Add authentication and role-based access

👨‍💻 Author

Kuldip Singh

IT Professional | AI Enthusiast | Cloud Learner
Python
SQL
AI Development
AWS Cloud
IT Support
Product Management
