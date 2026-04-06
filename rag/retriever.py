import numpy as np
from rag.embedder import get_embeddings

def retrieve(query, index, data, top_k=4):
    query_embedding = get_embeddings([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)
    results = [data[i] for i in indices[0]]
    return results