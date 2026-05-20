from retrieval.hybrid_retriever import hybrid_retrieve


def test_hybrid_retrieval():
    query = "hallucination"

    docs = hybrid_retrieve(query)

    assert len(docs) > 0

    first_doc = docs[0].page_content.lower()

    assert "hallucination" in first_doc