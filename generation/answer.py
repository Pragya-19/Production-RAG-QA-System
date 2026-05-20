from retrieval.hybrid_retriever import hybrid_retrieve
from retrieval.reranker import rerank


def answer_question(question: str):
    retrieved_docs = hybrid_retrieve(question, k=3)
    top_docs = rerank(question, retrieved_docs, top_n=2)

    answer_parts = []

    for doc in top_docs:
        source = doc.metadata.get("source", "unknown")
        chunk_id = doc.metadata.get("chunk_id", "unknown")

        answer_parts.append(
            f"{doc.page_content} [source: {source}, chunk_id: {chunk_id}]"
        )

    return {
        "question": question,
        "answer": " ".join(answer_parts),
        "contexts": [doc.page_content for doc in top_docs],
        "sources": [doc.metadata for doc in top_docs],
    }


if __name__ == "__main__":
    result = answer_question("What should QA teams test?")

    print("\nQUESTION:")
    print(result["question"])

    print("\nANSWER:")
    print(result["answer"])

    print("\nSOURCES:")
    for source in result["sources"]:
        print(source)