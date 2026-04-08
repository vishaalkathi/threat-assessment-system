from rag.embedder import get_embeddings
from rag.vector_store import create_index

def load_data():
    with open("rag/data/knowledge.txt", "r", encoding="utf-8") as f:
        data = [line.strip() for line in f if line.strip()]
    return data

def build_db():
    data = load_data()

    if not data:
        raise ValueError("knowledge.txt is empty")

    embeddings = get_embeddings(data)
    index = create_index(embeddings)
    return index, data