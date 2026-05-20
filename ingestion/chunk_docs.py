from langchain_text_splitters import RecursiveCharacterTextSplitter
from ingestion.load_docs import load_documents


def chunk_documents():
    docs = load_documents()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", ".", " ", ""],
    )

    chunks = splitter.split_documents(docs)

    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = f"chunk_{i}"

    return chunks


if __name__ == "__main__":
    chunks = chunk_documents()

    print(f"Created {len(chunks)} chunks")

    print("\nFIRST CHUNK:\n")
    print(chunks[0].page_content)

    print("\nMETADATA:\n")
    print(chunks[0].metadata)