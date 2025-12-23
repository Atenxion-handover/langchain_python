# `source_tuning/self_query_retriever.ipynb`

Notebook: `source_tuning/self_query_retriever.ipynb`

## What it does

Demonstrates metadata-aware retrieval using LangChain’s **SelfQueryRetriever** on top of a Qdrant vector store:

- Build a “query constructor” chain that converts natural language into a structured query (filters + optional limit).
- Use that structured query to retrieve documents based on both semantic similarity and metadata constraints.

The notebook also includes a RAG + tool-calling scaffold and an optional “Get Sources” pass similar to `related_sources.ipynb`.

## Workflow (step-by-step)

1. **Import Necessary Modules**
   - Imports LangChain, Qdrant translator utilities, and helper entry points.
2. **Define Functions and Schema**
   - Defines tools (via `@tool`) used by the tool-calling part of the notebook.
3. **Create Tool Collection**
   - Collects tools and binds them to the LLM.
4. **Initiate Retriever**
   - Builds a retriever via helpers for the RAG portion (and separate self-query retriever later).
5. **Initiate LLM**
   - Creates the chat model via helpers.
6. **Create Instructions for RAG Chain**
   - Defines contextualization and QA prompts.
7. **Create a RAG Chain Combined with Tool Calling**
   - Executes tool calls when emitted and re-invokes LLM with tool outputs.
8. **Invoke the Chain**
   - Runs example questions.
9. **Self-query retriever setup**
   - Defines metadata fields (e.g., `year`, `genre`, `director`, `rating`) and a content description.
   - Builds a query-constructor prompt and parser that outputs a structured query.
   - Instantiates `SelfQueryRetriever(...)` over a Qdrant vector store via `QdrantTranslator(...)`.
10. **Get Sources**
   - Optional provenance extraction similar to the `related_sources.ipynb` notebook.

## Notes

- Requires Qdrant connectivity via environment variables used by helpers (`QDRANT_URL`, `QDRANT_API_KEY`).
- Self-query retrieval quality depends heavily on metadata consistency and the LLM’s ability to generate correct filters.

