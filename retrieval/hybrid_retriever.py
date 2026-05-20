from retrieval.vector_store import load_vector_store
from retrieval.bm25 import BM25Retriever


def hybrid_retrieve(query: str, k: int = 3):
    vectorstore = load_vector_store()
    bm25 = BM25Retriever()

    vector_docs = vectorstore.similarity_search(query, k=k)
    bm25_docs = bm25.retrieve(query, k=k)

    seen = set()
    combined = []

    for doc in vector_docs + bm25_docs:
        key = doc.metadata.get("chunk_id")

        if key not in seen:
            combined.append(doc)
            seen.add(key)

    return combined[:k]


if __name__ == "__main__":
    query = "What should QA teams test?"

    docs = hybrid_retrieve(query)

    print(f"\nQUERY:\n{query}\n")

    for i, doc in enumerate(docs):
        print(f"\nRESULT {i + 1}")
        print("-" * 40)
        print(doc.page_content)
        print(doc.metadata)