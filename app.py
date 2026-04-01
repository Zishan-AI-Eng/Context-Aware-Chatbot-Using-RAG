
import streamlit as st
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import wikipedia

st.set_page_config(page_title="RAG Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 RAG Chatbot — AI/ML Knowledge Base")
st.markdown("Ask me anything about **Machine Learning, Deep Learning, NLP, Transformers** and more!")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vectorstore" not in st.session_state:
    with st.spinner("⏳ Loading Knowledge Base... Please wait..."):
        topics = [
            "Machine learning", "Deep learning",
            "Natural language processing", "Artificial neural network",
            "Transformer (machine learning)", "Large language model",
            "Retrieval-augmented generation", "Artificial intelligence"
        ]
        docs = []
        for topic in topics:
            try:
                page = wikipedia.page(topic, auto_suggest=False)
                docs.append({"title": topic, "content": page.content})
            except:
                pass

        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        all_chunks = []
        for doc in docs:
            chunks = splitter.split_text(doc["content"])
            for chunk in chunks:
                all_chunks.append(Document(
                    page_content=chunk,
                    metadata={"source": doc["title"]}
                ))

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        st.session_state.vectorstore = Chroma.from_documents(
            documents=all_chunks,
            embedding=embeddings,
            persist_directory=None
        )
        st.session_state.llm = ChatGroq(
            model_name="llama-3.3-70b-versatile",
            temperature=0.7,
            api_key=os.environ["GROQ_API_KEY"]
        )
    st.success("✅ Knowledge Base Loaded!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything about AI/ML..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            retriever = st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3})
            docs = retriever.invoke(prompt)
            context = "\n\n".join([doc.page_content for doc in docs])
            sources = list(set([doc.metadata["source"] for doc in docs]))

            messages = [
                {"role": "system", "content": f"""You are a helpful AI assistant.
Answer the question based on the context provided.
If you dont know, say you dont know.
Context:
{context}"""}
            ]
            for msg in st.session_state.chat_history:
                messages.append(msg)
            messages.append({"role": "user", "content": prompt})

            response = st.session_state.llm.invoke(messages)
            answer = response.content

            st.session_state.chat_history.append({"role": "user", "content": prompt})
            st.session_state.chat_history.append({"role": "assistant", "content": answer})

            full_response = f"{answer}\n\n📚 **Sources:** {', '.join(sources)}"
            st.markdown(full_response)
            st.session_state.messages.append({"role": "assistant", "content": full_response})
