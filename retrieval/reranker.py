def rerank(query: str, docs, top_n: int = 3):
    """
    Simple placeholder reranker.

    Later this can be upgraded to:
    - Cohere Rerank
    - Cross-encoder reranker
    - LLM-based reranker
    """
    return docs[:top_n]