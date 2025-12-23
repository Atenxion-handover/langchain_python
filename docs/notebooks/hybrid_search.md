# `hybrid_search.ipynb`

Notebook: `hybrid_search.ipynb`

## What it does

Demonstrates “hybrid” retrieval on Elasticsearch using dense vectors with hybrid mode enabled, then runs a standard RAG answer step on the retrieved context.

## Workflow (step-by-step)

1. **Load Env**
   - Loads `.env` variables (Elasticsearch + OpenAI + Langfuse, as applicable).
2. **Get Embeddings**
   - Creates OpenAI embeddings for dense vector indexing/search.
3. **Use Elasticsearch Hybrid Search**
   - Creates an `ElasticsearchStore` with `DenseVectorStrategy(hybrid=True)`.
   - Creates a retriever over the Elasticsearch index (`index_name="test"`).
4. **Define LLM**
   - Instantiates the chat model via `helpers.llm_integrations.get_llm(...)`.
5. **Create Contextualize Chain**
   - Turns chat-history-dependent questions into standalone queries.
6. **Create Retrieval Chain**
   - Retrieves top-k documents from the hybrid Elasticsearch retriever.
7. **Create QA Chain**
   - Answers strictly from the retrieved context.
8. **Token Usage Callback**
   - Collects token usage for the run.
9. **Langfuse Callback**
   - Adds tracing when configured.
10. **Create Final Chain (Contextualize → Retrieval → Q&A)**
   - Composes the full runnable chain.
11. **Invoke Chain**
   - Executes sample questions and prints results.

## Notes

- Requires `ELASTIC_CLOUD_ID` and `ELASTIC_API_KEY`.
- Assumes the Elasticsearch index (`index_name="test"`) already contains content compatible with the retriever configuration.

