# `elastic_elser_model.ipynb`

Notebook: `elastic_elser_model.ipynb`

## What it does

Demonstrates sparse semantic retrieval on Elasticsearch using the built-in **ELSER** model via `text_expansion`.

This notebook keeps the same overall RAG structure as the Chroma-based examples, but swaps the retriever implementation to Elasticsearch sparse vectors.

## Workflow (step-by-step)

1. **Load Env**
   - Loads `.env` variables (Elasticsearch Cloud ID + API key, Langfuse keys if used).
2. **Use Elasticsearch With ELSER Embedding Model**
   - Creates an `ElasticsearchStore` with `SparseVectorStrategy(model_id=".elser_model_2")`.
   - Exposes a similarity retriever (`k=top_k`).
3. **Define LLM**
   - Instantiates the chat model using `helpers.llm_integrations.get_llm(...)`.
4. **Create Contextualize Chain**
   - Rewrites question with chat history into a standalone question.
5. **Create Retrieval Chain**
   - Retrieves top-k documents from Elasticsearch.
6. **Create QA Chain**
   - Answers using retrieved context only.
7. **Token Usage Callback**
   - Captures token usage from the LLM calls.
8. **Langfuse Callback**
   - Enables tracing when credentials are present.
9. **Create Final Chain (Contextualize → Retrieval → Q&A)**
   - Composes end-to-end runnable chain.
10. **Invoke Chain**
   - Runs sample questions to validate retrieval and response generation.

## Notes

- Requires `ELASTIC_CLOUD_ID` and `ELASTIC_API_KEY`.
- Requires the ELSER model to be available in the target Elasticsearch cluster.

