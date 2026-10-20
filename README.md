# RAG Radar

A local-first retrieval-augmented generation baseline that keeps the retrieval layer transparent. It indexes Markdown documents with TF-IDF, returns the most relevant passages, and formats an answer context with file-and-line citations for an LLM or human reviewer.

## Run

```bash
python -m rag_radar.cli --docs examples --query "What is edge inference?"
```

No API key is required. Run tests with `python -m unittest discover -s tests`.

## Why this exists

RAG systems are easier to debug when retrieval can be inspected independently from generation. This project gives you a small evaluation surface for chunk size, overlap, ranking quality, and citation coverage before adding an LLM.
