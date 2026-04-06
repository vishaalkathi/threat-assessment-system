import faiss
import numpy as np

def create_index(embeddings):
    embeddings = np.array(embeddings, dtype="float32")
    embeddings = np.atleast_2d(embeddings)

    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index