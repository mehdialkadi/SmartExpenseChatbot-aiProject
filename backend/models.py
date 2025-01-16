from flask import app
import numpy as np
import openai
import google.generativeai as genai
import faiss
from backend.database import load_corpus_from_db

# Configuration
openai.api_key = "OPENAI-API-KEY" # Please replace with your own API key.
genai.configure(api_key="GOOGLE-GEMINI-API-KEY") # Please replace with your own API key.
embedding_model_name = "text-embedding-3-large"
db_path = "data/expenses.db"

# Step 1: Load and Index Corpus from SQLite
def index_corpus(corpus):
    """Generate embeddings and index the corpus using FAISS."""
    texts = [f"{row['description']} - Category: {row['category']} - Amount: ${row['amount']} - Date: ${row['date']} - Transaction Type: ${row['transaction_type']}" for row in corpus]
    embeddings = []
    for text in texts:
        response = openai.Embedding.create(model=embedding_model_name, input=text)
        embeddings.append(response["data"][0]["embedding"])
    embeddings = np.array(embeddings)

    # Create FAISS index
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return index, texts

# Step 2: Query and Retrieve Relevant Transactions
def retrieve_transactions(query, index, corpus, top_k=None):
    """Retrieve relevant transactions based on the query."""
    # Generate query embedding
    response = openai.Embedding.create(model=embedding_model_name, input=query)
    query_embedding = np.array(response["data"][0]["embedding"]).reshape(1, -1)

    # Search FAISS index
    distances, indices = index.search(query_embedding, top_k)

    # Retrieve relevant rows
    results = [corpus[idx] for idx in indices[0]]
    return results

# Step 3: Generate Response Using Gemini
def generate_response(query, retrieved_context):
    """Generate response using Gemini."""
    # Concatenate retrieved context
    context = "\n".join(retrieved_context)
    prompt = f"Context:\n{context}\n\nQuestion: {query}"
    print(context)
    
    # Use Gemini to generate content
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Step 4: Integrate the RAG Process
def retrieve_and_generate(query, db_path=db_path, top_k=5):
    # Load corpus from database
    corpus = load_corpus_from_db(db_path)

    # Index the corpus
    index, texts = index_corpus(corpus)

    # Retrieve relevant transactions
    retrieved = retrieve_transactions(query, index, texts, top_k)

    # Generate response
    response = generate_response(query, retrieved)
    return response
