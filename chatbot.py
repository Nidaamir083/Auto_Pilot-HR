import google.generativeai as genai
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from database import get_employees, get_leaves

# Initialize embedding model (only once)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def setup_gemini(api_key):
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-2.0-flash")

# Build FAISS vector store from policy text chunks
def build_vector_store(policy_texts):
    embeddings = embedding_model.encode(policy_texts)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings, policy_texts

# Retrieve most relevant chunks
def search_docs(index, query, policy_texts, top_k=3):
    query_embedding = embedding_model.encode([query])
    D, I = index.search(query_embedding, top_k)
    return [policy_texts[i] for i in I[0]]

# Ask Gemini with context
def ask_gemini(model, query, index=None, policy_texts=None):
    employees = get_employees()
    leaves = get_leaves()

    retrieved_docs = ""
    if index and policy_texts:
        top_chunks = search_docs(index, query, policy_texts)
        retrieved_docs = "\n".join(top_chunks)

    context = f"""
You are an HR Assistant chatbot. Use the following context to answer the query.

Company Policies:
{retrieved_docs}

Employee Data:
{employees}

Leave Data:
{leaves}

User Query:
{query}

Answer clearly and concisely.
"""
    response = model.generate_content(context)
    return response.text

