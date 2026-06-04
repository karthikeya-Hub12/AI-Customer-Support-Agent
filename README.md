# AI Customer Support Agent using LangGraph

## Project Overview

The AI Customer Support Agent is an intelligent customer service application built using LangGraph, LangChain, FastAPI, Streamlit, and OpenRouter LLMs. It automates customer query handling by leveraging Large Language Models (LLMs) and a company knowledge base to provide accurate, context-aware responses.

This project demonstrates the integration of Generative AI with modern backend and frontend technologies to create a scalable customer support solution.

---

## Features

* AI-powered customer support assistant
* LangGraph workflow orchestration
* OpenRouter LLM integration
* Company knowledge base support
* Context-aware response generation
* FastAPI REST API backend
* Interactive Swagger API documentation
* Streamlit web-based chat interface
* Real-time customer query handling
* Modular and extensible architecture

---

## Tech Stack

### Programming Language

* Python

### AI & LLM Frameworks

* LangChain
* LangGraph
* OpenRouter

### Backend

* FastAPI
* Uvicorn

### Frontend

* Streamlit

### Development Tools

* Git
* GitHub
* VS Code

---

## Project Structure

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

## Installation Steps

### 1. Clone Repository

```bash
git clone https://github.com/karthikeya-Hub12/AI-Customer-Support-Agent.git
cd AI-Customer-Support-Agent
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
```

---

## Running the Application

### Start FastAPI Backend

```bash
uvicorn api:api --reload
```

Open Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Start Streamlit UI

```bash
streamlit run ui.py
```

Open:

```text
http://localhost:8501
```

---

## Example Queries

* What is your refund policy?
* How can I contact support?
* What are your business hours?
* What is your shipping policy?
* How long does delivery take?

---

## API Endpoint

### POST /chat

Request:

```json
{
  "question": "What is your refund policy?"
}
```

Response:

```json
{
  "response": "Refunds are processed within 7 business days."
}
```

---

## Future Improvements

* Conversation memory
* Multi-agent workflows
* Sentiment analysis
* Order tracking integration
* Database connectivity
* Authentication and authorization
* Cloud deployment (Render/AWS/Azure)
* RAG (Retrieval-Augmented Generation)
* Analytics dashboard

---

## Key Skills Demonstrated

* Generative AI
* Large Language Models (LLMs)
* LangChain
* LangGraph
* Prompt Engineering
* FastAPI
* REST API Development
* Streamlit
* Python Development
* Git & GitHub

---

## Author

**Thaty Karthikeya**

GitHub: https://github.com/karthikeya-Hub12
