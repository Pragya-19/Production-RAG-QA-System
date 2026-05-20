from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_documents(folder: str = "data/docs"):
    docs = []

    for path in Path(folder).glob("*"):
        if path.suffix.lower() == ".pdf":
            docs.extend(PyPDFLoader(str(path)).load())

        elif path.suffix.lower() in [".txt", ".md"]:
            docs.extend(
                TextLoader(
                    str(path),
                    encoding="utf-8"
                ).load()
            )

    return docs