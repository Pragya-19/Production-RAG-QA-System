\# Production RAG QA System



A production-style Retrieval-Augmented Generation system designed for AI-QA use cases.



\## Features



\- Document ingestion

\- Text chunking

\- Local HuggingFace embeddings

\- FAISS vector search

\- BM25 keyword search

\- Hybrid retrieval

\- Reranker placeholder

\- Citation-based answers

\- FastAPI endpoint

\- Pytest validation



\## Architecture



User Question  

→ Hybrid Retrieval  

→ Reranking  

→ Context Selection  

→ Citation-Based Answer  

→ API Response



\## Why this matters for AI QA



AI-QA professionals need to test more than UI behavior. They need to validate retrieval quality, grounding, hallucination risk, citation correctness, and regression behavior.



This project demonstrates:



\- Retrieval validation

\- Citation validation

\- API testing

\- Regression testing

\- Grounded answer generation



\## Run locally



```bash

python -m venv .venv

.venv\\Scripts\\activate

pip install -r requirements.txt

python -m retrieval.vector\_store

uvicorn app.main:app --reload



Open:



http://127.0.0.1:8000/docs

Run tests

pytest

Current limitations

Uses extractive answer generation

No LLM-based synthesis yet

Reranker is a placeholder

Evaluation metrics not yet integrated

