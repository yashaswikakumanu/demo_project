from langchain.embeddings import OpenAIEmbeddings
import faiss
import numpy as np
from elasticsearch import Elasticsearch

embeddings_model = OpenAIEmbeddings()
es = Elasticsearch("http://localhost:9200")

def generate_embedding(text):
    return embeddings_model.embed_query(text)

# FAISS setup
dimension = 1536  # OpenAI embedding size
index = faiss.IndexFlatL2(dimension)

def store_in_faiss(text):
    vector = np.array([generate_embedding(text)], dtype=np.float32)
    index.add(vector)

def search_similar_reports(query_text):
    query_vector = np.array([generate_embedding(query_text)], dtype=np.float32)
    distances, indices = index.search(query_vector, k=1)
    return indices[0]

# Elasticsearch functions
def log_health_data(user_id, food, steps, notes):
    doc = {"user_id": user_id, "food": food, "steps": steps, "notes": notes}
    es.index(index="health_tracking", document=doc)

def get_past_logs(user_id):
    query = {"query": {"match": {"user_id": user_id}}}
    results = es.search(index="health_tracking", body=query)
    return results['hits']['hits']
