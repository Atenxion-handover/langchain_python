# Notebook Documentation

This folder contains a short “what it does” + “workflow” document for every `.ipynb` notebook in this repo.

## Common prerequisites

Most notebooks load credentials from a local `.env` (via `python-dotenv` or `helpers.config.Config`). Depending on the notebook, you may need:

- `OPENAI_API_KEY` (OpenAI chat + embeddings)
- `CHROMA_API_KEY`, `CHROMA_TENANT`, `CHROMA_DATABASE` (Chroma Cloud-backed notebooks)
- `ELASTIC_CLOUD_ID`, `ELASTIC_API_KEY` (Elasticsearch-backed notebooks)
- `COHERE_API_KEY` (Cohere reranker, only for reranker notebooks when using Cohere models)
- `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_BASEURL` (Langfuse tracing in some notebooks)
- `POSTGRES_CONNECTION_STRING` (structured/unstructured routing notebooks)
- `QDRANT_URL`, `QDRANT_API_KEY` (Qdrant-backed notebooks via helpers)
- `MISTRAL_API_KEY` (Mistral function calling notebook)
- `TAVILY_API_KEY` (CRAG notebook web-search tool)

Some notebooks also use local model runtimes (e.g. Ollama) and require you to have those installed and running.

## Index

### Root notebooks

- `docs/notebooks/adaptive_rag.md` — Adaptive RAG with query classification + iterative follow-up retrieval.
- `docs/notebooks/base_workflow.md` — Minimal “contextualize → retrieve → answer” RAG workflow on Chroma.
- `docs/notebooks/basic_retrieval_flow.md` — Base workflow + token usage + Langfuse callbacks.
- `docs/notebooks/crag.md` — Corrective RAG (CRAG): grade retrieval, optionally web-search, refine context.
- `docs/notebooks/elastic_elser_model.md` — Elasticsearch sparse retrieval using ELSER (`text_expansion`).
- `docs/notebooks/hybrid_search.md` — Elasticsearch dense retrieval with hybrid mode enabled.
- `docs/notebooks/using_custom_reranker.md` — RAG where retrieval step is reranked by a custom reranker.
- `docs/notebooks/using_reranker.md` — RAG where retrieval step is reranked via `helpers.reranker_integration`.

### `function_calling/`

- `docs/notebooks/function_calling/function_calling_and_question_generation.md` — RAG + tool calling + follow-up question generation.
- `docs/notebooks/function_calling/mistral_function_calling.md` — Function calling pattern using the Mistral client.
- `docs/notebooks/function_calling/openai_function_calling.md` — Function calling pattern using the OpenAI client.

### `notebooks/` (Elasticsearch retrieval strategy comparisons)

- `docs/notebooks/notebooks/just_dense.md` — Dense-only retrieval (Elasticsearch dense vectors).
- `docs/notebooks/notebooks/just_sparse.md` — Sparse-only retrieval (ELSER `text_expansion`).
- `docs/notebooks/notebooks/just_bm25.md` — BM25-only retrieval (lexical search).
- `docs/notebooks/notebooks/dense_bm25.md` — Hybrid dense+BM25 using Elasticsearch strategy.
- `docs/notebooks/notebooks/sparse_bm25.md` — Hybrid sparse+BM25 using a custom RRF query.
- `docs/notebooks/notebooks/dense_sparse.md` — Ensemble retriever combining dense and sparse indices.

### `source_tuning/`

- `docs/notebooks/source_tuning/related_sources.md` — Source attribution pass: infer which sources an answer came from.
- `docs/notebooks/source_tuning/self_query_retriever.md` — Self-query retriever (metadata-aware retrieval) with Qdrant.

### `structured_unstructured_routing/`

- `docs/notebooks/structured_unstructured_routing/structured_unstructured_routing.md` — Route a question to SQL vs RAG (LLM router and embedding router).
- `docs/notebooks/structured_unstructured_routing/structured_unstructured_routing_with_two_store.md` — Same routing idea, plus a “two store” variant.
- `docs/notebooks/structured_unstructured_routing/langgraph_routing.md` — Same routing idea implemented as a LangGraph state machine.

