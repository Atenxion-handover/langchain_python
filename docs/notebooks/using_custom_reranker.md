# `using_custom_reranker.ipynb`

Notebook: `using_custom_reranker.ipynb`

## What it does

Adds a reranking step into the retrieval part of a Chroma-backed RAG workflow:

- Retrieve an initial set of candidates from Chroma.
- Rerank (compress) the candidate set using a reranker model.
- Answer using the reranked context.

## Workflow (step-by-step)

1. **Load Env**
   - Loads `.env` variables (OpenAI, Chroma, Langfuse; reranker keys if needed).
2. **Get Embeddings**
   - Creates OpenAI embeddings for Chroma similarity search.
3. **Create Retriever**
   - Connects to a Chroma collection (`collection_name="chat_history_test"`) and creates a base retriever.
4. **Create Reranker**
   - Creates a “custom reranker” component and configures how many documents to keep after reranking.
5. **Define LLM**
   - Uses `helpers.llm_integrations.get_llm(...)` for the answer model.
6. **Create Contextualize Chain**
   - Rewrites questions into standalone queries when chat history exists.
7. **Create QA Chain**
   - Builds the answer prompt that only uses `{context}`.
8. **Create Retrieval Chain (Pass Custom Reranker Instead of Retriever)**
   - Swaps the base retriever for the reranker-wrapped retriever when building the retrieval stage.
9. **Token Usage Callback**
   - Captures token usage.
10. **Langfuse Callback**
   - Enables tracing.
11. **Create Final Chain (Contextualize → Retrieval → Q&A)**
   - Composes the pipeline end-to-end.
12. **Invoke Chain**
   - Runs sample questions and prints outputs.

## Notes

- Depending on the reranker model chosen, you may need additional credentials (e.g. `COHERE_API_KEY`) or local model availability.

