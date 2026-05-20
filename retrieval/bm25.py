from rank_bm25 import BM25Okapi
from ingestion.chunk_docs import chunk_documents


class BM25Retriever:
    def __init__(self):
        self.docs = chunk_documents()

        self.tokenized_docs = [
            doc.page_content.lower().split()
            for doc in self.docs
        ]

        self.bm25 = BM25Okapi(self.tokenized_docs)

    def retrieve(self, query: str, k: int = 3):
        tokenized_query = query.lower().split()

        scores = self.bm25.get_scores(tokenized_query)

        ranked = sorted(
            zip(self.docs, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return [doc for doc, score in ranked[:k]]


if __name__ == "__main__":
    retriever = BM25Retriever()

    query = "retrieval quality"

    docs = retriever.retrieve(query)

    print(f"\nQUERY:\n{query}\n")

    for i, doc in enumerate(docs):
        print(f"\nRESULT {i + 1}")
        print("-" * 40)
        print(doc.page_content)
        print(doc.metadata)