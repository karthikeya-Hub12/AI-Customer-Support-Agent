# 🤖 AI Customer Support Agent using LangGraph

## 📌 Overview

The AI Customer Support Agent is a Generative AI application designed to automate customer support interactions. It leverages Large Language Models (LLMs) to understand customer queries and provide accurate, context-aware responses based on company information.

The project combines LangGraph for workflow orchestration, LangChain for LLM integration, FastAPI for backend APIs, and Streamlit for an interactive user interface. It demonstrates how modern AI technologies can be used to build intelligent customer service solutions.

---

## 🚀 Key Features

* AI-powered customer support assistant
* Natural language understanding and response generation
* LangGraph-based workflow management
* OpenRouter LLM integration
* FastAPI REST API backend
* Interactive Streamlit web interface
* Company knowledge base integration
* Real-time query handling
* Modular and scalable architecture
* Easy to extend for real-world business applications

---

## 🎯 Problem Statement

Customer support teams often spend significant time answering repetitive questions related to refunds, returns, shipping, business hours, and contact information.

This project automates these interactions by providing instant AI-generated responses, improving efficiency and customer experience while reducing manual workload.

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit Interface
 │
 ▼
FastAPI Backend
 │
 ▼
LangGraph Workflow
 │
 ▼
OpenRouter LLM
 │
 ▼
Knowledge Base
 │
 ▼
AI Response
```

---

## 🛠️ Technology Stack

### Programming Language

* Python

### AI & LLM Frameworks

* LangChain
* LangGraph
* OpenRouter

### Backend Development

* FastAPI
* Uvicorn

### Frontend Development

* Streamlit

### Version Control

* Git
* GitHub

---

## 📂 Project Structure

```text
AI-Customer-Support-Agent/
│
├── agent.py
├── api.py
├── app.py
├── customer_graph.py
├── langgraph_agent.py
├── memory_agent.py
├── support_data.py
├── test_agent.py
├── ui.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/karthikeya-Hub12/AI-Customer-Support-Agent.git
cd AI-Customer-Support-Agent
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project directory:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

**Note:** Never upload your `.env` file to GitHub.

---

## ▶️ Running the Application

### Start the FastAPI Backend

```bash
uvicorn api:api --reload
```

API Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Start the Streamlit Interface

```bash
streamlit run ui.py
```

Application URL:

```text
http://localhost:8501
```

---

## 💬 Sample Queries

Users can interact with the assistant using queries such as:

* What is your refund policy?
* What are your business hours?
* How can I contact support?
* What is your shipping policy?
* How long does delivery take?
* How can I return a product?

---

## 🔌 API Example

### Request

```json
{
  "question": "What is your refund policy?"
}
```

### Response

```json
{
  "response": "Refunds are processed within 7 business days."
}
```

---

## 🎯 Skills Demonstrated

* Generative AI
* Large Language Models (LLMs)
* LangChain
* LangGraph
* Prompt Engineering
* FastAPI
* REST API Development
* Streamlit
* Python Programming
* API Integration
* Git & GitHub

---

## 🔮 Future Enhancements

* Conversation Memory
* Multi-Agent Workflows
* Sentiment Analysis
* Order Tracking Integration
* Database Connectivity
* Retrieval-Augmented Generation (RAG)
* Authentication & Authorization
* Cloud Deployment (AWS, Azure, Render)
* Analytics Dashboard

---

## 📄 Resume Description

**AI Customer Support Agent using LangGraph**

Developed an AI-powered customer support assistant using LangGraph, LangChain, OpenRouter, FastAPI, and Streamlit. Built REST APIs for intelligent customer query handling, integrated a company knowledge base for context-aware response generation, and designed an interactive web interface for real-time customer interactions.

---

## 👨‍💻 Author

**Thaty Karthikeya**
