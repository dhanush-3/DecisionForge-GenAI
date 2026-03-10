from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model once (important for performance)
model = SentenceTransformer('all-MiniLM-L6-v2')

documents = [
    "SWOT analysis helps identify strengths and weaknesses.",
    "Porter's Five Forces analyze competitive environment.",
    "Lean startup focuses on MVP and iteration."
]

# Create embeddings
embeddings = model.encode(documents)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(embeddings))


def retrieve_context(query):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=2)

    # Return formatted context string instead of list
    results = [documents[i] for i in I[0]]
    return "\n".join(results)