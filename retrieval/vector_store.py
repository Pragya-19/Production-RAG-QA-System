from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from ingestion.chunk_docs import chunk_documents


INDEX_PATH = "data/vector_index"


def build_vector_store():
    chunks = chunk_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local(INDEX_PATH)

    return vectorstore


def load_vector_store():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True,
    )


if __name__ == "__main__":
    build_vector_store()
    print("Vector index created")