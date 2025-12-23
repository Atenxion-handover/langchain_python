# `using_reranker.ipynb`

Notebook: `using_reranker.ipynb`

## What it does

Adds a reranking step into a Chroma-backed RAG workflow using `helpers.reranker_integration.get_reranker`:

- Retrieve candidates from the base retriever.
- Rerank/compress results with a cross-encoder reranker (HuggingFace) or Cohere reranker.
- Answer using the reranked context.

## Workflow (step-by-step)

1. **Load Env**
   - Loads `.env` variables (OpenAI, Chroma, Langfuse, and optional reranker keys).
2. **Get Embeddings**
   - Creates OpenAI embeddings.
3. **Create Retriever**
   - Connects to a Chroma collection (`collection_name="test"`) and creates a base similarity retriever.
4. **Create Reranker**
   - Wraps the base retriever with a compression retriever that reranks documents and keeps the top N.
5. **Define LLM**
   - Uses `helpers.llm_integrations.get_llm(...)` for answer generation.
6. **Create Contextualize Chain**
   - Optional “standalone question” rewriting step when chat history exists.
7. **Create QA Chain**
   - Answers using only the retrieved/reranked context.
8. **Create Retrieval Chain (Pass Reranker Instead of Retriever)**
   - Uses the reranker-wrapped retriever in the retrieval stage.
9. **Token Usage Callback**
   - Captures token usage.
10. **Langfuse Callback**
   - Enables tracing.
11. **Create Final Chain (Contextualize → Retrieval → Q&A)**
   - Composes the runnable chain.
12. **Invoke Chain**
   - Runs example questions.

## Notes

- If you choose a Cohere reranker model, set `COHERE_API_KEY`.
- If you choose a HuggingFace cross-encoder reranker, the model must be available locally (downloaded by your environment).

