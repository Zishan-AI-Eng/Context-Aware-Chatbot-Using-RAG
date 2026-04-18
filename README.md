# 🤖 Context-Aware RAG Chatbot — AI/ML Knowledge Base

> An intelligent conversational chatbot that retrieves answers from a vectorized knowledge base using Retrieval-Augmented Generation (RAG), powered by Groq's Llama 3.3 70B and deployed with Streamlit.

---
## 🌐 Live Demo

👉 **[Click here to try the chatbot live!](https://context-aware-chatbot-using-rag-bzhtfcq2xwuatlcch3ddyb.streamlit.app/
)**


## 📌 Objective

Build a context-aware chatbot that:
- Remembers conversation history across multiple turns
- Retrieves relevant information from a vectorized document store
- Generates accurate, grounded answers using a Large Language Model (LLM)
- Deploys as an interactive web application using Streamlit

---

## 🏗️ Methodology / Approach

### 1. 📚 Knowledge Base Creation
- Loaded **8 Wikipedia articles** covering AI/ML topics:
  - Machine Learning, Deep Learning, NLP, Artificial Neural Networks
  - Transformers, Large Language Models, RAG, Artificial Intelligence

### 2. ✂️ Text Chunking
- Used `RecursiveCharacterTextSplitter` with:
  - `chunk_size = 500`
  - `chunk_overlap = 50`
- Generated **3064 text chunks** from all documents

### 3. 🗄️ Vector Store (ChromaDB)
- Embedded all chunks using `HuggingFace all-MiniLM-L6-v2`
- Stored embeddings in **ChromaDB** (persistent vector store)
- Enables fast semantic similarity search at query time

### 4. 🧠 LLM Integration (Groq)
- Used **Llama 3.3 70B** via Groq API (free & fast)
- Retrieves top **3 most relevant chunks** per query
- Passes retrieved context + chat history to LLM for answer generation

### 5. 💬 Conversation Memory
- Maintains full **chat history** across conversation turns
- Chatbot remembers previous questions and answers
- Enables follow-up questions and context-aware responses

### 6. 🌐 Deployment
- Deployed using **Streamlit** as an interactive web UI
- Publicly accessible via **Cloudflare Tunnel**

---

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| 🧠 LLM | Groq — Llama 3.3 70B |
| 🔗 Framework | LangChain |
| 🗄️ Vector Store | ChromaDB |
| 📐 Embeddings | HuggingFace all-MiniLM-L6-v2 |
| 📚 Knowledge Base | Wikipedia (8 Articles) |
| 🌐 Deployment | Streamlit + Cloudflare Tunnel |
| 💻 Platform | Google Colab |

---

## 📊 Key Results

| Metric | Value |
|---|---|
| 📚 Knowledge Base | 8 Wikipedia Articles |
| ✂️ Total Chunks | 3064 |
| 🧪 Test Cases | 5 |
| 🎯 Success Rate | 100% |
| 💬 Context Memory | ✅ Active |
| 🌐 Live Deployment | ✅ Streamlit |

---

## 🧪 Evaluation Results

| # | Question | Sources Retrieved | Answer Length |
|---|---|---|---|
| 1 | What is deep learning? | Deep learning, AI | 64 words |
| 2 | How do transformers work in NLP? | Transformer, ANN | 252 words |
| 3 | What is the difference between ML and AI? | ML, AI | 254 words |
| 4 | Explain retrieval augmented generation | RAG, LLM | 326 words |
| 5 | What are neural networks used for? | DL, ANN, AI | 181 words |

**Overall Success Rate: 100% ✅**

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/Zishan-AI-Eng/Context-Aware-Chatbot-Using-RAG
cd Context-Aware-Chatbot-Using-RAG
```

### 2. Install Dependencies
```bash
pip install langchain langchain-community langchain-groq langchain-core langchain-text-splitters chromadb sentence-transformers wikipedia streamlit pyngrok
```

### 3. Set Your Groq API Key
```bash
export GROQ_API_KEY="your_groq_api_key_here"
```

### 4. Run the Chatbot
```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
rag-chatbot-aiml/
│
├── app.py                  # Streamlit web application
├── rag_chatbot.ipynb       # Main Jupyter Notebook
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## 💡 Key Learnings

- How **RAG** improves LLM accuracy by grounding answers in real documents
- How **ChromaDB** stores and retrieves vector embeddings efficiently
- How **conversation memory** enables multi-turn contextual dialogues
- How to deploy AI apps publicly using **Streamlit + Cloudflare Tunnel**

---

## 👨‍💻 Author

**Your Name**
- 🌐 GitHub: [Dev-ZishanKhan](https://github.com/Zishan-AI-Eng)
- 💼 LinkedIn: [ZishanCoder](https://www.linkedin.com/in/zishan-coderx-048483370/)

---

